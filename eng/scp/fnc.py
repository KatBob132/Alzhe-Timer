from json import load as lod
from random import *
from math import *

# math

def clp(num, min=None, max=None):
    if min != None:
        if num < min:
            num = min
    if max != None:
        if num > max:
            num = max
    
    return num

# data

def jsn_dat(loc):
    return lod(open(loc))

# color

def cfg_clr(clr):
    return (clp(int(clr[0]), 0, 255), clp(int(clr[1]), 0, 255), clp(int(clr[2]), 0, 255))