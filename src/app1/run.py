#!/usr/bin/env python 

# A test python code

class app1:
    """ simple arithmetic calculation
    """
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b
    def plus(self):
        """return a + b
        """
        c = self.a + self.b
        print "%s: %d + %d = %d"%(__name__, self.a, self.b, c)
    def multiplication(self):
        """return a * b
        """
        c = self.a * self.b
        print "%s: %d * %d = %d"%(__name__, self.a, self.b, c)
