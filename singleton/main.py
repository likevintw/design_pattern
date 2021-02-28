
"""
singleton
whatever how many time for calling a class
with multiple instances, they will indicate 
the same instance.

"""

import logging
logging.basicConfig(level=logging.INFO)


class Singleton(object):
    class A():
        def __init__(self):
            logging.debug("A.__init__")
            self.val = None

        def __str__(self):
            logging.debug("A.__str__")
            return "{0!r} {1}".format(self, self.val)

    instance = None
    def __new__(cls):
        logging.debug("SingletonObject.__new__")
        if not Singleton.instance:
            Singleton.instance = Singleton.A()
        return Singleton.instance

    def __getattr__(self, name):
        logging.debug("Singleton.__getattr__")
        return getattr(self.instance, name)
    
    def __setattr__(self, name):
        logging.debug("Singleton.__setattr__")
        return setattr(self.instance, name)


if __name__ == "__main__":

    print("\n")
    tester_1 = Singleton()
    tester_1.val = "tester1"
    print("test1: ", tester_1)
    
    print("\n")
    tester_2 = Singleton()
    print("test1: ", tester_1)
    tester_2.val = "tester2"
    print("test1: ", tester_1)
    print("test2: ", tester_2)