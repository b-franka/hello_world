#!/usr/bin/env python

import sys

def greet(name):
    print ("Hello", sys.argv[1], "!")

if len(sys.argv[1:]) ==0:
    print ("Hello World!")
for arg in sys.argv[1:]:
    greet(arg)
