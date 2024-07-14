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

def bnd_clr(clr_1, clr_2, wgt_1, wgt_2):
    clr_1 = cfg_clr(clr_1)
    clr_2 = cfg_clr(clr_2)

    wgt_1 = int(wgt_1)
    wgt_2 = int(wgt_2)

    clr_ret = [0, 0, 0]

    for a in range(3):
        for b in range(wgt_1):
            clr_ret[a] += clr_1[a]
        
        for c in range(wgt_2):
            clr_ret[a] += clr_2[a]
        
        clr_ret[a] = round(clr_ret[a] / (wgt_1  + wgt_2))

    return clr_ret