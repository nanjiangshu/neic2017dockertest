import os
import sys

from app1.run import app1
from app2.run import app2

if __name__ == '__main__':
    ap1 = app1(3,8)
    ap2 = app2(4)
    ap1.plus()
    ap1.multiplication()
    ap2.sin()
    ap2.cos()
    ap2.pow10()
    ap2.pow16()
    ap2.tan()

