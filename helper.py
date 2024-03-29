# When to use class methods and when to use static methods?

class Item:
    @staticmethod
    def isinteger():
        '''
        This should do something that has a relationship
        with the class, but not something that must be
        unique per instance.
        '''

    @classmethod
    def instantiaterom-something(cls):
        '''
        This should be something that has a relationship
        with the class but usually are used to manipulate
        different structures of data to instantiate
        objects, like csv.
        '''
