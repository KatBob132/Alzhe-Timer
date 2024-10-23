from speech_recognition import Recognizer as rec, Microphone as mic
from random import randrange as rr
from json import load as lod
from gtts import gTTS as gtt
from random import *
from math import *

# math

def ran(min, max):
    return rr(min, max + 1)

def clp(num, min=None, max=None):
    if min != None:
        if num < min:
            num = min
    if max != None:
        if num > max:
            num = max
    
    return num

def whl(num, max, min, zer=False):
    while num > max or num < min:
        if num > max:
            num -= max

            if zer:
                num -= 1
        else:
            if zer:
                num += max + 1
            else:
                num += max
    
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

def hit(xy, box):
    xy = (int(xy[0]), int(xy[1]))
    box = ((int(box[0][0]), int(box[0][1])), (int(box[1][0]), int(box[1][1])))
    hit_d = False

    if xy[0] >= box[0][0] and xy[0] <= box[0][0] + box[1][0]:
        if xy[1] >= box[0][1] and xy[1] <= box[0][1] + box[1][1]:
            hit_d = True
    
    return hit_d

# data

def jsn_dat(loc):
    return lod(open(loc))

def spk(txt, fil):
    txt = str(txt)
    fil = str(fil)

    voc = gtt(text=txt, lang="en")
    voc.save("eng/nte/" + fil + ".mp3")

def spc():
    txt = None
    rc = rec()

    with mic() as sur:
        aud_txt = rc.listen(sur)

        try:
            txt = rc.recognize_google(aud_txt)
        except:
            txt = "?"
    
    return txt

# color

def cfg_clr(clr):
    return (clp(int(clr[0]), 0, 255), clp(int(clr[1]), 0, 255), clp(int(clr[2]), 0, 255))

def bld_clr(clr_1, clr_2, clr_phs):
    bld_d_clr = []

    for a in range(3):
        bld_d_clr.append(clr_1[a] + (clr_2[a] - clr_1[a]) * clr_phs)

    return cfg_clr(bld_d_clr)

tot_lrp = 0.2
tot_inc = 0.0075