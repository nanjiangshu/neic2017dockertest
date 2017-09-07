#!/usr/bin/env python
# A test python code
import math

class app2:
    """simple math
    """
    def __init__(self, x=10):
        self.x = x
    def sin(self):
        c = math.sin(self.x)
        print "%s: sin(%g) = %g"%(__name__, self.x, c)
    def cos(self):
        c = math.cos(self.x)
        print "%s: cos(%g) = %g"%(__name__, self.x, c)
    def tan(self):
        c = math.tan(self.x)
        print "%s: tan(%g) = %g"%(__name__, self.x, c)
    def pow10(self):
        c = math.pow(10, self.x)
        print "%s: pow10(%g) = %g"%(__name__, self.x, c)
    def pow16(self):
        c = math.pow(16, self.x)
        print "%s: pow16(%g) = %g"%(__name__, self.x, c)
