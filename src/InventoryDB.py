
"""
Some useful links:

Reading and writing to .csv files:      https://docs.python.org/2/library/csv.html
Dictionaries:                           https://www.tutorialspoint.com/python/python_dictionary.htm
Extending classes and inheritance:      https://docs.python.org/2/tutorial/classes.html     (section 9.5)
Observer pattern:                       https://en.wikipedia.org/wiki/Observer_pattern
"""



class InventoryDB:
    """ Database class """

    def __init__(self, db=None):
        """ intitialise database, with a database file in csv format at the filepath specified by db """

        self.db = self.parseCSV(db)
        self.updateSubs = []            # list of classifiers that care about changes to the database

    def parseCSV(self, data):
        # TODO use open as csvfile. See: https://docs.python.org/2/library/csv.html
        """
        Resets database with a given .csv file
        :param data: .csv file containing database core information
        :param meta: .csv file containing metadata such as pre-classified information such as A-B-C categorisations etc.
        :return: dictionary of Item objects, indexed by the item's name
        """

        if data is None:
            # TODO Throw an error here
            return

        # TODO parse the csv

    def sale(self, items):
        """
        Updates the database after a sale, and notifies subscribing classifiers of the change

        :param items: list of items sold
        :return: invoice information
        """

        # if the items in sale are passed with positive quantities, make them negative so classifiers work properly
        for item in items:
            if item.quantity > 0:
                item.quantity = -item.quantity

        # notify classifiers of the change
        for classifier in self.updateSubs:
            classifier.classify(items)


    def purchase(self, items):
        """
        Updates the database after a purchase
        :param items: list of items purchased
        :return: boolean audit result for validating purchase against some record
        """
        # if the items in sale are passed with negative quantities, make them negative so classifiers work properly
        for item in items:
            if item.quantity < 0:
                item.quantity = -item.quantity

        for classifier in self.updateSubs:
            classifier.classify(items)
        return True

    def writeCSV(self):
        """
        Writes a new database.csv file based on current state, moving old files to log
        """

    def getItem(self, item):
        """
        Returns an item object
        :param item: key for item lookup
        :return: item object matching key
        """

    def getCategory(self, classifier):
        """
        Find all items in a given classifier
        :param classifier: lookup key
        :return: all items matching classifier
        """


class BasicClassifier:
        """
        Abstract classifier class, made by ClassifierFactory. Extended classes should implement the methods in this.
        Classifiers should write to metadata files so uncommon classifiers don't need to persist in ram.

        Classifier classes can store metadata however they want, as long as they can then parse their own metadata
        to return requested classifications.

        Utilise a metadata file so the classified list can be rebuilt if the classifier is killed or restarted,
        you can store meta information however you want, as long as the parseMeta function can use it.

        :param db: database containing database to classify
        :return:
        """

        def __init__(self, db=None, meta=None):
            """
            Classify a database on initialisation, and store the metadata file location internally.

            :param db: list of item objects to be classified
            :param meta: file path to metadata file to be written to
            """
            self.inClass = {}
            self.meta = meta                    # Metadata file location
            self.db = db                        # store a reference to the db and open the read in the metadata file
            self.parseMeta()                    # Generate inClass from metadata

        def parseMeta(self):
            """
            Open the metadata file and put pre-classified items into self.inClass (from self.db)
            """

        def writeMeta(self):
            """
            Write the current state of the classifier to the metadata file, call this whenever the classifier changes
            state (adding or removing classified items) to ensure metadata is accurate in case the system restarts
            """

        def classify(self, items=None):
            """
            Logical classification function,
            :param items: Items to classify (if None run on the whole db, use this on updates to save on computation)
            """


class BasicItem:
    """
    Generic item object for storing intrinsic information about an item (code, price, number in stock, etc).
    Extend this class to add more complicated information if needed for strange items, but should be able to jus
    """
    def __init__(self, foo=None, bar=None, quantity=0, key=None):
        """ Initialise item attributes """
        self.foo = foo              # example attributes, change to be appropriate
        self.bar = bar
        self.quantity = quantity    # Items must have this so sale and purchase can differentiate
        self.key = key              # This is needed for accessing items in dictionaries, probably the item's code


if __name__ == "__main__":

    core = InventoryDB('data.csv')
