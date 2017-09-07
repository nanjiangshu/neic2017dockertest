# this script is for testing OpenShift continuous integration
import os
import sys
import random
import time

from app1.run import app1
from app2.run import app2

if __name__ == '__main__':
    # create a while loop for continuous running
    loop = 0
    while 1:
        loop += 1
        a = 1
        b = 100
        x1 = random.randint(a,b)
        x2 = random.randint(a,b)
        x3 = random.randint(a,b)
        ap1 = app1(x1,x2)
        ap2 = app2(x3)
        print "\nloop = %d, x1 = %d, x2 = %d, x3 = %d"%(loop, x1,x2,x3)
        ap1.plus()
        ap1.multiplication()
        ap2.sin()
        ap2.cos()
        ap2.pow10()
        ap2.pow16()
        ap2.tan()
        time.sleep(10)

