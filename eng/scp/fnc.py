from json import load as lod
from gtts import gTTS as gtt
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

def whl(num, max, zer=False):
    while num > max:
        num -= max

        if zer:
            num -= 1
    
    return num

def lrp(sar, end, val, dlt, inc):
    sar = float(sar)
    end = float(end)

    val = float(val)
    dlt = float(dlt)
    inc = float(inc)

    if abs(end - sar) <= inc:
        sar = end
    else:
        sar += (end - sar) / (val / dlt)
    
    return sar

# data

def jsn_dat(loc):
    return lod(open(loc))

def spk(txt, fil):
    txt = str(txt)
    fil = str(fil)

    voc = gtt(text=txt, lang="en")
    voc.save("eng/nte/" + fil + ".mp3")

# color

def cfg_clr(clr):
    return (clp(int(clr[0]), 0, 255), clp(int(clr[1]), 0, 255), clp(int(clr[2]), 0, 255))

def bld_clr(clr_1, clr_2, clr_phs):
    bld_d_clr = []

    for a in range(3):
        bld_d_clr.append(clr_1[a] + (clr_2[a] - clr_1[a]) * clr_phs)

    return cfg_clr(bld_d_clr)