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

def clp_whl(num, max, zer=False):
    while num > max or num < 0:
        if num > max:
            num -= max

            if zer:
                num -= 1
        else:
            num += max
    
    return num

def min(num):
    return clp_whl(num, 59, True)

def hur_mon(num):
    return clp_whl(num, 12)

# data

def jsn_dat(loc):
    return lod(open(loc))

# color

def cfg_clr(clr):
    return (clp(int(clr[0]), 0, 255), clp(int(clr[1]), 0, 255), clp(int(clr[2]), 0, 255))

def bld_clr(clr_1, clr_2, clr_phs):
    bld_d_clr = []

    for a in range(3):
        bld_d_clr.append(clr_1[a] + (clr_2[a] - clr_1[a]) * clr_phs)

    return cfg_clr(bld_d_clr)