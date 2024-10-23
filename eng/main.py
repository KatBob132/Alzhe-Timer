from scp.obj import *
from scp.utl import *
from scp.fnc import *

from pygame.locals import *
import pygame as pg

from calendar import monthrange as mon
from datetime import datetime as dat
from time import time as tme
from json import dump as dmp
from sys import exit as ext

scn = {}

scn["siz"] = (288, 384)
scn["pix-siz"] = 3

scn["srf"] = pg.Surface(scn["siz"])

scn["win"] = None
scn["win-bck"] = None

siz = (scn["siz"][0] * scn["pix-siz"], scn["siz"][1] * scn["pix-siz"])
clr = jsn_dat("eng/dat/clr.json")
txt = fnt("eng/dat/fnt.ttf", scn["srf"])

tme_cal = {}
fps_cal = {}

tme_cal["str"] = tme()
tme_cal["now"] = 0
tme_cal["dlt"] = 0

fps_cal["fps"] = 0
fps_cal["fps-lit"] = []
fps_cal["fps-avg"] = 0
 
# View Reminders

hst_clr = clr["pink"]
bck_clr = clr["black"]
cer_clr = clr["white"]

ret = None
fix = 0
tmr = jsn_dat("eng/dat/tmr.json")

tht = {}

tht["lit"] = tmr["tht"]
tht["cur"] = 0
tht["wnt"] = 0

tht["phs"] = [0, True]
tht["tmr"] = [0, 3]

viw = {}

viw["scr"] = 0
viw["spc"] = 0
viw["siz"] = None
viw["sld"] = [0, False, False, False]
viw["del"] = []
viw["box"] = ((0, 0), (0, 0))

viw["bld-ver"] = [0, 0]
viw["bld"] = 0

dte = {}

dte["now"] = dat.now()

dte["mon"] = dte["now"].month
dte["day"] = dte["now"].day
dte["wek"] = dte["now"].weekday()
dte["yer"] = dte["now"].year

dte["hor"] = dte["now"].hour
dte["min"] = dte["now"].minute
dte["sec"] = dte["now"].microsecond

dte["per"] = None

if dte["hor"] >= 12:
    dte["per"] = "PM"
    dte["hor"] -= 12
else:
    dte["per"] = "AM"

bts = wrk(hst_clr, bck_clr, cer_clr, scn["srf"], txt)

bts.add_grp("mnu", True)

bts.add_grp("tht")
bts.add_grp("tod")
bts.add_grp("evy")
bts.add_grp("far")
bts.add_grp("viw")

### Menu

bts.add_bts("mnu", "Thought", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 49), (True, True))
bts.add_bts("mnu", "Today", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 15), (True, True))
bts.add_bts("mnu", "Everyday", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 19), (True, True))
bts.add_bts("mnu", "Faraway", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 53), (True, True))
bts.add_bts("mnu", "View", (scn["siz"][0] // 2, scn["siz"][1] - 48), (True, True))

bts.add_icn("mnu", "Reminder's", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 82), (scn["siz"][0] // 2, scn["siz"][1] + 9), (True, True))

### Thought

bts.add_bts("tht", "Thought", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 32), (True, True))
bts.add_bts("tht", "Done", (scn["siz"][0] // 2, scn["siz"][1] // 2), (True, True))
bts.add_bts("tht", "Cancel", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 30), (True, True))

### Today

bts.add_bts("tod", "12", (scn["siz"][0] // 2 - 36, scn["siz"][1] // 2 - 43), (True, True), True)
bts.add_bts("tod", "59", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 43), (True, True), True)
bts.add_bts("tod", "AM", (scn["siz"][0] // 2 + 36, scn["siz"][1] // 2 - 43), (True, True))

bts.add_icn("tod", ":", (scn["siz"][0] // 2 - 18, scn["siz"][1] // 2 - 43), (-3, scn["siz"][1] // 2 - 43), (True, True))
bts.add_icn("tod", ":", (scn["siz"][0] // 2 + 18, scn["siz"][1] // 2 - 43), (scn["siz"][0] + 2, scn["siz"][1] // 2 - 43), (True, True))

bts.add_bts("tod", "Note", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 13), (True, True))
bts.add_bts("tod", "Done", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 17), (True, True))
bts.add_bts("tod", "Cancel", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 47), (True, True))

## Everyday

bts.add_bts("evy", "", (scn["siz"][0] // 2 - 72, scn["siz"][1] // 2 - 51), (True, True))
bts.add_bts("evy", "", (scn["siz"][0] // 2 - 48, scn["siz"][1] // 2 - 51), (True, True))
bts.add_bts("evy", "", (scn["siz"][0] // 2 - 24, scn["siz"][1] // 2 - 51), (True, True))

bts.add_bts("evy", "", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 51), (True, True))

bts.add_bts("evy", "", (scn["siz"][0] // 2 + 24, scn["siz"][1] // 2 - 51), (True, True))
bts.add_bts("evy", "", (scn["siz"][0] // 2 + 48, scn["siz"][1] // 2 - 51), (True, True))
bts.add_bts("evy", "", (scn["siz"][0] // 2 + 72, scn["siz"][1] // 2 - 51), (True, True))

bts.add_icn("evy", "MO", (scn["siz"][0] // 2 - 72, scn["siz"][1] // 2 - 28), (-13, scn["siz"][1] // 2 - 28), (True, True))
bts.add_icn("evy", "TU", (scn["siz"][0] // 2 - 48, scn["siz"][1] // 2 - 76), (scn["siz"][0] + 14, scn["siz"][1] // 2 - 76), (True, True))
bts.add_icn("evy", "WE", (scn["siz"][0] // 2 - 24, scn["siz"][1] // 2 - 28), (-13, scn["siz"][1] // 2 - 28), (True, True))
bts.add_icn("evy", "TH", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 76), (scn["siz"][0] + 14, scn["siz"][1] // 2 - 76), (True, True))
bts.add_icn("evy", "FR", (scn["siz"][0] // 2 + 24, scn["siz"][1] // 2 - 28), (-13, scn["siz"][1] // 2 - 28), (True, True))
bts.add_icn("evy", "SA", (scn["siz"][0] // 2 + 48, scn["siz"][1] // 2 - 76), (scn["siz"][0] + 14, scn["siz"][1] // 2 - 76), (True, True))
bts.add_icn("evy", "SU", (scn["siz"][0] // 2 + 72, scn["siz"][1] // 2 - 28), (-13, scn["siz"][1] // 2 - 28), (True, True))

bts.add_bts("evy", "12", (scn["siz"][0] // 2 - 36, scn["siz"][1] // 2), (True, True), True)
bts.add_bts("evy", "59", (scn["siz"][0] // 2, scn["siz"][1] // 2), (True, True), True)
bts.add_bts("evy", "AM", (scn["siz"][0] // 2 + 36, scn["siz"][1] // 2), (True, True))

bts.add_icn("evy", ":", (scn["siz"][0] // 2 - 18, scn["siz"][1] // 2), (-3, scn["siz"][1] // 2), (True, True))
bts.add_icn("evy", ":", (scn["siz"][0] // 2 + 18, scn["siz"][1] // 2), (scn["siz"][0] + 2, scn["siz"][1] // 2), (True, True))

bts.add_bts("evy", "Note", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 30), (True, True))
bts.add_bts("evy", "Done", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 60), (True, True))
bts.add_bts("evy", "Cancel", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 90), (True, True))

### Farawau

bts.add_bts("far", "12", (scn["siz"][0] // 2 - 36, scn["siz"][1] // 2 - 60), (True, True), True)
bts.add_bts("far", "12", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 60), (True, True), True)
bts.add_bts("far", "9999", (scn["siz"][0] // 2 + 49, scn["siz"][1] // 2 - 60), (True, True), True)

bts.add_icn("far", ":", (scn["siz"][0] // 2 - 18, scn["siz"][1] // 2 - 60), (-3, scn["siz"][1] // 2 - 60), (True, True))
bts.add_icn("far", ":", (scn["siz"][0] // 2 + 18, scn["siz"][1] // 2 - 60), (scn["siz"][0] + 2, scn["siz"][1] // 2 - 60), (True, True))

bts.add_bts("far", "12", (scn["siz"][0] // 2 - 36, scn["siz"][1] // 2 - 30), (True, True), True)
bts.add_bts("far", "59", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 30), (True, True), True)
bts.add_bts("far", "AM", (scn["siz"][0] // 2 + 36, scn["siz"][1] // 2 - 30), (True, True))

bts.add_icn("far", ":", (scn["siz"][0] // 2 - 18, scn["siz"][1] // 2 - 30), (-3, scn["siz"][1] // 2 - 30), (True, True))
bts.add_icn("far", ":", (scn["siz"][0] // 2 + 18, scn["siz"][1] // 2 - 30), (scn["siz"][0] + 2, scn["siz"][1] // 2 - 30), (True, True))

bts.add_bts("far", "Note", (scn["siz"][0] // 2, scn["siz"][1] // 2), (True, True))
bts.add_bts("far", "Done", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 30), (True, True))
bts.add_bts("far", "Cancel", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 60), (True, True))

### View

bts.add_bts("viw", "Back", (scn["siz"][0] // 2, scn["siz"][1] - 58), (True, False))
bts.add_bts("viw", "Delete All", (scn["siz"][0] // 2, scn["siz"][1] - 28), (True, False))

pg.init()
pg.mixer.init()

dpy = pg.display.set_mode(siz, DOUBLEBUF)
pg.display.set_caption("Alzhe Timer")
fps = pg.time.Clock()

mos_dat = {}

mos_dat["xy"] = (pg.mouse.get_pos()[0] // scn["pix-siz"], pg.mouse.get_pos()[1] // scn["pix-siz"])
mos_dat["btt"] = [False, False, False]
mos_dat["chg"] = [[], 0]

while True:
    dpy.fill(cer_clr)
    scn["srf"].fill(cer_clr)

    pg.mouse.set_visible(False)

    mos_dat["xy"] = (pg.mouse.get_pos()[0] // scn["pix-siz"], pg.mouse.get_pos()[1] // scn["pix-siz"])

    tme_cal["now"] = tme()
    tme_cal["dlt"] = (tme_cal["now"] - tme_cal["str"])
    tme_cal["str"] = tme()

    fps_cal["fps"] = 1 / tme_cal["dlt"]
    fps_cal["fps-lit"].append(fps_cal["fps"])

    if len(fps_cal["fps-lit"]) > round(fps_cal["fps"]):
        fps_cal["fps-lit"].pop(0)

    fps_cal["fps-avg"] = round(sum(fps_cal["fps-lit"]) / len(fps_cal["fps-lit"]))

    dte["now"] = dat.now()

    dte["mon"] = dte["now"].month
    dte["day"] = dte["now"].day
    dte["wek"] = dte["now"].weekday()
    dte["yer"] = dte["now"].year

    dte["hor"] = dte["now"].hour
    dte["min"] = dte["now"].minute
    dte["sec"] = dte["now"].microsecond

    dte["per"] = None

    if dte["hor"] >= 12:
        dte["per"] = "PM"
        dte["hor"] -= 12
    else:
        dte["per"] = "AM"

    # pg.draw.rect(scn["srf"], clr["red"], pg.Rect(scn["siz"][0] // 2, 0, 1, scn["siz"][1]))
    # pg.draw.rect(scn["srf"], clr["red-dark"], pg.Rect(scn["siz"][0] // 2 + 1, 0, 1, scn["siz"][1]))
    # pg.draw.rect(scn["srf"], clr["red"], pg.Rect(0, scn["siz"][1] // 2, scn["siz"][0], 1))
    # pg.draw.rect(scn["srf"], clr["red-dark"], pg.Rect(0, scn["siz"][1] // 2 + 1, scn["siz"][0], 1))

    pg.draw.rect(scn["srf"], bck_clr, pg.Rect(0, scn["siz"][1] - 30, scn["siz"][0], 30))

    if len(tmr["tht"]) > 1:
        if tht["cur"] != None:
            tht["lit"] = tmr["tht"]
            
            if tht["phs"][1]:
                tht["tmr"][0] += tme_cal["dlt"]
            
            if int(tht["tmr"][0]) >= tht["tmr"][1]:
                tht["tmr"][0] = 0
                tht["wnt"] = ran(0, len(tht["lit"]) - 1)
            
            if tht["wnt"] != tht["cur"]:
                tht["phs"][0] = lrp(tht["phs"][0], 1, tot_lrp, tme_cal["dlt"], tot_inc)
                tht["phs"][1] = False

                if tht["phs"][0] == 1:
                    tht["cur"] = tht["wnt"]
            else:
                tht["phs"][0] = lrp(tht["phs"][0], 0, tot_lrp, tme_cal["dlt"], tot_inc)

                if tht["phs"][0] == 0:
                    tht["phs"][1] = True

            try:
                txt.drw(tht["lit"][tht["cur"]], (scn["siz"][0] // 2, scn["siz"][1] - 15), 20, bld_clr(cer_clr, bck_clr, tht["phs"][0]), (0, 2), bld_clr(hst_clr, bck_clr, tht["phs"][0]), (True, True))
            except:
                continue
    
    if bts.wrk_cur["cur"] != "mnu":
        pg.draw.rect(scn["srf"], cer_clr, pg.Rect(0, scn["siz"][1] - 30, scn["siz"][0], 30 * bts.wrk_grp_s["mnu"]["sld"]))
    else:
        pg.draw.rect(scn["srf"], cer_clr, pg.Rect(0, scn["siz"][1] - 30, scn["siz"][0], 30 * bts.wrk_grp_s["mnu"]["sld"]))

    try:
        for typ in tmr:
            if typ != "tht":
                for a in range(len(tmr[typ])):
                    if typ == "tod" and tmr[typ][a]["tme"] == [dte["hor"], dte["min"], dte["per"]]:
                        spk(tmr[typ][a]["nte"], tmr[typ][a]["nme"])

                        pg.mixer.music.load("eng/nte/" + tmr[typ][a]["nme"] + ".mp3")
                        pg.mixer.music.play()

                        tmr[typ].pop(a)
                    if typ == "evy"and tmr[typ][a]["act"][dte["wek"]] and tmr[typ][a]["tme"] == [dte["hor"], dte["min"], dte["per"]] and fix != dte["min"]:
                        spk(tmr[typ][a]["nte"], tmr[typ][a]["nme"])

                        pg.mixer.music.load("eng/nte/" + tmr[typ][a]["nme"] + ".mp3")
                        pg.mixer.music.play()

                        fix = dte["min"]
                    if typ == "far" and tmr[typ][a]["dte"] == [dte["mon"], dte["day"], dte["yer"]] and tmr[typ][a]["tme"] == [dte["hor"], dte["min"], dte["per"]]:
                        spk(tmr[typ][a]["nte"], tmr[typ][a]["nme"])

                        pg.mixer.music.load("eng/nte/" + tmr[typ][a]["nme"] + ".mp3")
                        pg.mixer.music.play()

                        tmr[typ].pop(a)
    except:
        continue

    ret = bts.upt(mos_dat["xy"], mos_dat["btt"][0], tme_cal["dlt"])

    if ret != None:
        if bts.get_num(ret[0], ret[1]) == False:
            mos_dat["btt"][0] = False

        match ret[0]:
            case "mnu":
                match ret[1]:
                    case 0:
                        bts.chg_grp("tht")

                        bts.chg_bts("tht", 0, "Thought")
                    case 1:
                        bts.chg_grp("tod")

                        bts.chg_bts("tod", 0, dte["hor"])
                        bts.chg_bts("tod", 1, dte["min"])
                        bts.chg_bts("tod", 2, dte["per"])
                        bts.chg_bts("tod", 3, "Note")
                    case 2:
                        bts.chg_grp("evy")

                        for a in range(7):
                            bts.chg_bts("evy", a, "")
                        
                        bts.chg_bts("evy", 7, dte["hor"])
                        bts.chg_bts("evy", 8, dte["min"])
                        bts.chg_bts("evy", 9, dte["per"])
                        bts.chg_bts("evy", 10, "Note")
                    case 3:
                        bts.chg_grp("far")

                        bts.chg_bts("far", 0, dte["mon"])
                        bts.chg_bts("far", 1, dte["day"])
                        bts.chg_bts("far", 2, dte["yer"])
                        bts.chg_bts("far", 3, dte["hor"])
                        bts.chg_bts("far", 4, dte["min"])
                        bts.chg_bts("far", 5, dte["per"])
                        bts.chg_bts("far", 6, "Note")
                    case 4:
                        viw["scr"] = 0
                        viw["sld"][0] = 0

                        bts.chg_grp("viw")
            
            case "tht":
                match ret[1]:
                    case 0:
                        bts.chg_bts(ret[0], ret[1], spc())
                        bts.chg_clk(ret[0], ret[1])
                    case 1:
                        tmr[ret[0]].append(bts.get_bts(ret[0], 0))

                        bts.chg_grp("mnu")
                    case 2:
                        bts.chg_grp("mnu")
            
            case "tod":
                match ret[1]:
                    case 0:
                        bts.chg_num(ret[0], ret[1], mos_dat["chg"][1], 12, 1)
                    case 1:
                        bts.chg_num(ret[0], ret[1], mos_dat["chg"][1], 59, 0, True)
                    case 2:
                        if bts.get_bts(ret[0], ret[1]) == "AM":
                            bts.chg_bts(ret[0], ret[1], "PM")
                        else:
                            bts.chg_bts(ret[0], ret[1], "AM")
                    case 3:
                        bts.chg_bts(ret[0], ret[1], spc())
                        bts.chg_clk(ret[0], ret[1])
                    case 4:
                        tmr[ret[0]].append({})
                        
                        tmr[ret[0]][-1]["tme"] = [int(bts.get_bts(ret[0], 0)), int(bts.get_bts(ret[0], 1)), bts.get_bts(ret[0], 2)]
                        tmr[ret[0]][-1]["nte"] = bts.get_bts(ret[0], 3)
                        tmr[ret[0]][-1]["nme"] = tmr[ret[0]][-1]["nte"] + "_" + ret[0] + "_" + str(len(tmr[ret[0]]) - 1)

                        bts.chg_grp("mnu")
                    case 5:
                        bts.chg_grp("mnu")
            
            case "evy":
                match ret[1]:
                    case 0:
                        if bts.get_bts(ret[0], ret[1]) == "":
                            bts.chg_bts(ret[0], ret[1], "")
                        else:
                            bts.chg_bts(ret[0], ret[1], "")
                    case 1:
                        if bts.get_bts(ret[0], ret[1]) == "":
                            bts.chg_bts(ret[0], ret[1], "")
                        else:
                            bts.chg_bts(ret[0], ret[1], "")
                    case 2:
                        if bts.get_bts(ret[0], ret[1]) == "":
                            bts.chg_bts(ret[0], ret[1], "")
                        else:
                            bts.chg_bts(ret[0], ret[1], "")
                    case 3:
                        if bts.get_bts(ret[0], ret[1]) == "":
                            bts.chg_bts(ret[0], ret[1], "")
                        else:
                            bts.chg_bts(ret[0], ret[1], "")
                    case 4:
                        if bts.get_bts(ret[0], ret[1]) == "":
                            bts.chg_bts(ret[0], ret[1], "")
                        else:
                            bts.chg_bts(ret[0], ret[1], "")
                    case 5:
                        if bts.get_bts(ret[0], ret[1]) == "":
                            bts.chg_bts(ret[0], ret[1], "")
                        else:
                            bts.chg_bts(ret[0], ret[1], "")
                    case 6:
                        if bts.get_bts(ret[0], ret[1]) == "":
                            bts.chg_bts(ret[0], ret[1], "")
                        else:
                            bts.chg_bts(ret[0], ret[1], "")
                    case 7:
                        bts.chg_num(ret[0], ret[1], mos_dat["chg"][1], 12, 1)
                    case 8:
                        bts.chg_num(ret[0], ret[1], mos_dat["chg"][1], 59, 0, True)
                    case 9:
                        if bts.get_bts(ret[0], ret[1]) == "AM":
                            bts.chg_bts(ret[0], ret[1], "PM")
                        else:
                            bts.chg_bts(ret[0], ret[1], "AM")
                    case 10:
                        bts.chg_bts(ret[0], ret[1], spc())
                        bts.chg_clk(ret[0], ret[1])
                    case 11:
                        tmr[ret[0]].append({})
                        
                        tmr[ret[0]][-1]["tme"] = [int(bts.get_bts(ret[0], 7)), int(bts.get_bts(ret[0], 8)), bts.get_bts(ret[0], 9)]
                        tmr[ret[0]][-1]["nte"] = bts.get_bts(ret[0], 10)
                        tmr[ret[0]][-1]["nme"] = tmr[ret[0]][-1]["nte"] + "_" + ret[0] + "_" + str(len(tmr[ret[0]]) - 1)
                        
                        tmr[ret[0]][-1]["act"] = []

                        for a in range(7):
                            if bts.get_bts("evy", a) == "":
                                tmr[ret[0]][-1]["act"].append(True)
                            else:
                                tmr[ret[0]][-1]["act"].append(False)
                            
                        bts.chg_grp("mnu")
                    case 12:
                        bts.chg_grp("mnu")

            case "far":
                match ret[1]:
                    case 0:
                        bts.chg_num(ret[0], ret[1], mos_dat["chg"][1], 12, 1)
                    case 1:
                        bts.chg_num(ret[0], ret[1], mos_dat["chg"][1], mon(int(bts.get_bts("far", 2)), int(bts.get_bts("far", 0)))[1], 1)
                    case 2:
                        bts.chg_num(ret[0], ret[1], mos_dat["chg"][1], 9999, 1)
                    case 3:
                        bts.chg_num(ret[0], ret[1], mos_dat["chg"][1], 12, 1)
                    case 4:
                        bts.chg_num(ret[0], ret[1], mos_dat["chg"][1], 59, 0, True)
                    case 5:
                        if bts.get_bts(ret[0], ret[1]) == "AM":
                            bts.chg_bts(ret[0], ret[1], "PM")
                        else:
                            bts.chg_bts(ret[0], ret[1], "AM")
                    case 6:
                        bts.chg_bts(ret[0], ret[1], spc())
                        bts.chg_clk(ret[0], ret[1])
                    case 7:
                        tmr[ret[0]].append({})
                        
                        tmr[ret[0]][-1]["dte"] = [int(bts.get_bts(ret[0], 0)), int(bts.get_bts(ret[0], 1)), int(bts.get_bts(ret[0], 2))]
                        tmr[ret[0]][-1]["tme"] = [int(bts.get_bts(ret[0], 3)), int(bts.get_bts(ret[0], 4)), bts.get_bts(ret[0], 5)]
                        tmr[ret[0]][-1]["nte"] = bts.get_bts(ret[0], 6)
                        tmr[ret[0]][-1]["nme"] = tmr[ret[0]][-1]["nte"] + "_" + ret[0] + "_" + str(len(tmr[ret[0]]) - 1)

                        bts.chg_grp("mnu")
                    case 8:
                        bts.chg_grp("mnu")

            case "viw":
                match ret[1]:
                    case 0:
                        bts.chg_grp("mnu")
                    case 1:
                        viw["sld"][1] = True
                        viw["sld"][2] = True
    
    viw["spc"] = 0

    if bts.wrk_cur["vis"] == "viw":
        for typ in tmr:
            for a in range(len(tmr[typ])):
                if tmr[typ][a] != "":
                    if typ == "tht":
                        viw["siz"] = txt.are(tmr[typ][a], 19, (0, 2))

                        if 37 + viw["spc"] + viw["siz"][1] + viw["scr"] < scn["siz"][1] - 65 and viw["spc"] + viw["scr"] > -1:
                            viw["bld-ver"][0] = (6 - clp((scn["siz"][1] - 65) - (37 + viw["spc"] + viw["siz"][1] + viw["scr"]), max=6)) / 6
                            viw["bld-ver"][1] = clp(6 - (viw["spc"] + viw["scr"] + 1), 0) / 6
                            viw["bld"] = max(viw["bld-ver"])
                            viw["box"] = ((scn["siz"][0] // 2 - viw["siz"][0] // 2 - 3, 31 + viw["spc"] + viw["scr"]), (viw["siz"][0] + 6, viw["siz"][1] + 6))

                            txt.drw(tmr[typ][a], (scn["siz"][0] // 2, 34 + viw["spc"] + viw["scr"]), 19, bld_clr(bck_clr, cer_clr, viw["bld"]), (0, 2), bld_clr(hst_clr, cer_clr, viw["bld"]), (True, False))    

                            if hit(mos_dat["xy"], viw["box"]):
                                viw["bld"] += 0.1

                                if mos_dat["btt"][0] and viw["sld"][0] == 0:
                                    viw["sld"][1] = True
                                    viw["del"].append((typ, a))
                            
                            viw["bld"] = clp(viw["bld"], max=1)

                            pg.draw.rect(scn["srf"], bld_clr(hst_clr, cer_clr, viw["bld"]), pg.Rect(scn["siz"][0] // 2 - viw["siz"][0] // 2 - 3, 31 + viw["spc"] + viw["scr"], viw["siz"][0] + 6, viw["siz"][1] + 6), 1)
                        
                        if a == len(tmr[typ]) - 1:
                            viw["spc"] += viw["siz"][1] + 13
                        else:
                            viw["spc"] += viw["siz"][1] + 12                        

                    if typ == "tod":
                        viw["siz-1"] = txt.are(tmr[typ][a]["nte"], 19, (0, 2))
                        viw["txt-1"] = str(tmr[typ][a]["tme"][0]) + ":" + str(tmr[typ][a]["tme"][1]) + " " + str(tmr[typ][a]["tme"][2])

                        viw["siz-2"] = txt.are(viw["txt-1"], 19, (0, 2))
                        viw["siz"] = [max([viw["siz-1"][0], viw["siz-2"][0]]), viw["siz-1"][1] + viw["siz-2"][1] + 2]

                        if 37 + viw["spc"] + viw["siz"][1] + viw["scr"] < scn["siz"][1] - 65 and viw["spc"] + viw["scr"] > -1:
                            viw["bld-ver"][0] = (6 - clp((scn["siz"][1] - 65) - (37 + viw["spc"] + viw["siz"][1] + viw["scr"]), max=6)) / 6
                            viw["bld-ver"][1] = clp(6 - (viw["spc"] + viw["scr"] + 1), 0) / 6
                            viw["bld"] = max(viw["bld-ver"])
                            viw["box"] = ((scn["siz"][0] // 2 - viw["siz"][0] // 2 - 3, 34 + viw["spc"] - 3 + viw["scr"]), (viw["siz"][0] + 6, viw["siz"][1] + 6))

                            txt.drw(tmr[typ][a]["nte"], (scn["siz"][0] // 2, 34 + viw["spc"] + viw["scr"]), 19, bld_clr(bck_clr, cer_clr, viw["bld"]), (0, 2), bld_clr(hst_clr, cer_clr, viw["bld"]), (True, False))
                            txt.drw(viw["txt-1"], (scn["siz"][0] // 2, 34 + viw["spc"] + viw["siz-1"][1] + 2 + viw["scr"]), 19, bld_clr(bck_clr, cer_clr, viw["bld"]), (0, 2), bld_clr(hst_clr, cer_clr, viw["bld"]), (True, False))

                            if hit(mos_dat["xy"], viw["box"]):
                                viw["bld"] += 0.1
                                
                                if mos_dat["btt"][0] and viw["sld"][0] == 0:
                                    viw["sld"][1] = True
                                    viw["del"].append((typ, a))

                            viw["bld"] = clp(viw["bld"], max=1)

                            pg.draw.rect(scn["srf"], bld_clr(hst_clr, cer_clr, viw["bld"]), pg.Rect(scn["siz"][0] // 2 - viw["siz"][0] // 2 - 3, 34 + viw["spc"] - 3 + viw["scr"], viw["siz"][0] + 6, viw["siz"][1] + 6), 1)

                        if a == len(tmr[typ]) - 1:
                            viw["spc"] += viw["siz"][1] + 13
                        else:
                            viw["spc"] += viw["siz"][1] + 12                        
                    
                    if typ == "evy":
                        viw["siz-1"] = txt.are(tmr[typ][a]["nte"], 19, (0, 2))
                        viw["txt-1"] = str(tmr[typ][a]["tme"][0]) + ":" + str(tmr[typ][a]["tme"][1]) + " " + str(tmr[typ][a]["tme"][2])
                        viw["siz-2"] = txt.are(viw["txt-1"], 19, (0, 2))

                        viw["txt-2"] = ""

                        for b in range(7):
                            if tmr[typ][a]["act"][b]:
                                viw["txt-2"] += ""
                            else:
                                viw["txt-2"] += ""
                            
                            if b < 6:
                                viw["txt-2"] += "/"

                        viw["siz-3"] = txt.are(viw["txt-2"], 19, (0, 2))
                        viw["siz"] = (max([viw["siz-1"][0], viw["siz-2"][0], viw["siz-3"][0]]), viw["siz-1"][1] + viw["siz-2"][1] + viw["siz-3"][1] + 4)

                        if 37 + viw["spc"] + viw["siz"][1] + viw["scr"] < scn["siz"][1] - 64 and viw["spc"] + viw["scr"] > -1:
                            viw["bld-ver"][0] = (6 - clp((scn["siz"][1] - 65) - (37 + viw["spc"] + viw["siz"][1] + viw["scr"]), max=6)) / 6
                            viw["bld-ver"][1] = clp(6 - (viw["spc"] + viw["scr"] + 1), 0) / 6
                            viw["bld"] = max(viw["bld-ver"])
                            viw["box"] = ((scn["siz"][0] // 2 - viw["siz"][0] // 2 - 3, 34 + viw["spc"] - 3 + viw["scr"]), (viw["siz"][0] + 6, viw["siz"][1] + 6))

                            txt.drw(tmr[typ][a]["nte"], (scn["siz"][0] // 2, 34 + viw["spc"] + viw["scr"]), 19, bld_clr(bck_clr, cer_clr, viw["bld"]), (0, 2), bld_clr(hst_clr, cer_clr, viw["bld"]), (True, False))    
                            txt.drw(viw["txt-1"], (scn["siz"][0] // 2, 34 + viw["spc"] + viw["siz-1"][1] + 2 + viw["scr"]), 19, bld_clr(bck_clr, cer_clr, viw["bld"]), (0, 2), bld_clr(hst_clr, cer_clr, viw["bld"]), (True, False))    
                            txt.drw(viw["txt-2"], (scn["siz"][0] // 2, 34 + viw["spc"] + viw["siz-1"][1] + viw["siz-2"][1] + 4 + viw["scr"]), 19, bld_clr(bck_clr, cer_clr, viw["bld"]), (0, 2), bld_clr(hst_clr, cer_clr, viw["bld"]), (True, False))

                            if hit(mos_dat["xy"], viw["box"]):
                                viw["bld"] += 0.1
                                
                                if mos_dat["btt"][0] and viw["sld"][0] == 0:
                                    viw["sld"][1] = True
                                    viw["del"].append((typ, a))
                            
                            viw["bld"] = clp(viw["bld"], max=1)

                            pg.draw.rect(scn["srf"], bld_clr(hst_clr, cer_clr, viw["bld"]), pg.Rect(scn["siz"][0] // 2 - viw["siz"][0] // 2 - 3, 34 + viw["spc"] - 3 + viw["scr"], viw["siz"][0] + 6, viw["siz"][1] + 6), 1)

                        if a == len(tmr[typ]) - 1:
                            viw["spc"] += viw["siz"][1] + 13
                        else:
                            viw["spc"] += viw["siz"][1] + 12                        
                    
                    if typ == "far":
                        viw["siz-1"] = txt.are(tmr[typ][a]["nte"], 19, (0, 2))
                        viw["txt-1"] = str(tmr[typ][a]["tme"][0]) + ":" + str(tmr[typ][a]["tme"][1]) + " " + str(tmr[typ][a]["tme"][2])
                        viw["siz-2"] = txt.are(viw["txt-1"], 19, (0, 2))

                        viw["txt-2"] = str(tmr[typ][a]["dte"][0]) + "/" + str(tmr[typ][a]["dte"][1]) + "/" + str(tmr[typ][a]["dte"][2])

                        viw["siz-3"] = txt.are(viw["txt-2"], 19, (0, 2))
                        viw["siz"] = (max([viw["siz-1"][0], viw["siz-2"][0], viw["siz-3"][0]]), viw["siz-1"][1] + viw["siz-2"][1] + viw["siz-3"][1] + 4)

                        if 37 + viw["spc"] + viw["siz"][1] + viw["scr"] < scn["siz"][1] - 65 and viw["spc"] + viw["scr"] > -1:
                            viw["bld-ver"][0] = (6 - clp((scn["siz"][1] - 65) - (37 + viw["spc"] + viw["siz"][1] + viw["scr"]), max=6)) / 6
                            viw["bld-ver"][1] = clp(6 - (viw["spc"] + viw["scr"] + 1), 0) / 6
                            viw["bld"] = max(viw["bld-ver"])
                            viw["box"] = ((scn["siz"][0] // 2 - viw["siz"][0] // 2 - 3, 34 + viw["spc"] - 3 + viw["scr"]), (viw["siz"][0] + 6, viw["siz"][1] + 6))

                            txt.drw(tmr[typ][a]["nte"], (scn["siz"][0] // 2, 34 + viw["spc"] + viw["scr"]), 19, bld_clr(bck_clr, cer_clr, viw["bld"]), (0, 2), bld_clr(hst_clr, cer_clr, viw["bld"]), (True, False))    
                            txt.drw(viw["txt-1"], (scn["siz"][0] // 2, 34 + viw["spc"] + viw["siz-1"][1] + 2 + viw["scr"]), 19, bld_clr(bck_clr, cer_clr, viw["bld"]), (0, 2), bld_clr(hst_clr, cer_clr, viw["bld"]), (True, False))    
                            txt.drw(viw["txt-2"], (scn["siz"][0] // 2, 34 + viw["spc"] + viw["siz-1"][1] + viw["siz-2"][1] + 4 + viw["scr"]), 19, bld_clr(bck_clr, cer_clr, viw["bld"]), (0, 2), bld_clr(hst_clr, cer_clr, viw["bld"]), (True, False))

                            if hit(mos_dat["xy"], viw["box"]):
                                viw["bld"] += 0.1
                                
                                if mos_dat["btt"][0] and viw["sld"][0] == 0:
                                    viw["sld"][1] = True
                                    viw["del"].append((typ, a))

                            pg.draw.rect(scn["srf"], bld_clr(hst_clr, cer_clr, viw["bld"]), pg.Rect(scn["siz"][0] // 2 - viw["siz"][0] // 2 - 3, 34 + viw["spc"] - 3 + viw["scr"], viw["siz"][0] + 6, viw["siz"][1] + 6), 1)

                        if a == len(tmr[typ]) - 1:
                            viw["spc"] += viw["siz"][1] + 13
                        else:
                            viw["spc"] += viw["siz"][1] + 12
            
        if viw["sld"][1]:
            if viw["sld"][2]:
                viw["sld"][0] = lrp(viw["sld"][0], 1, tot_lrp, tme_cal["dlt"], tot_inc)

                if round(viw["sld"][0], 2) >= 0.99:
                    tmr = {"tht": [""], "tod": [], "evy": [], "far": []} 
                if viw["sld"][0] == 1:
                    viw["sld"][2] = False
                    viw["sld"][1] = False
                    viw["sld"][0] = 0
            else:
                if viw["sld"][3]:
                    viw["sld"][0] = lrp(viw["sld"][0], 0, tot_lrp, tme_cal["dlt"], tot_inc)

                    if viw["sld"][0] == 0:
                        viw["sld"][3] = False
                        viw["sld"][1] = False
                else:
                    viw["sld"][0] = lrp(viw["sld"][0], 1, tot_lrp, tme_cal["dlt"], tot_inc)
                
                if round(viw["sld"][0], 2) >= 0.99:
                    try:
                        for a in range(len(viw["del"])):
                            tmr[viw["del"][a][0]].pop(viw["del"][a][1])
                            viw["del"].pop(a)
                    except:
                        continue

                if viw["sld"][0] == 1:
                    viw["sld"][3] = True

        pg.draw.rect(scn["srf"], clr["white"], pg.Rect(0, 31, scn["siz"][0] * max([bts.wrk_grp_s["viw"]["sld"], viw["sld"][0]]), scn["siz"][1] - 97))
    
    pg.draw.rect(scn["srf"], clr["green"], pg.Rect(mos_dat["xy"][0] - 3, mos_dat["xy"][1] - 3, 6, 6))

    txt.drw("Alzhe Timer", (scn["siz"][0] // 2, 2), 26, hst_clr, (0, 2), bck_clr, (True, False))

    for evt in pg.event.get():
        if evt.type == pg.QUIT:
            with open("eng/dat/tmr.json", "w") as f:
                dmp(tmr, f)

            pg.quit()
            ext()

        if evt.type == pg.KEYDOWN:                
            if evt.key == pg.K_ESCAPE:
                with open("eng/dat/tmr.json", "w") as f:
                    dmp(tmr, f)

                pg.quit()
                ext()
            
        if evt.type == pg.MOUSEBUTTONDOWN:
            for a in range(3):
                if evt.button == a + 1:
                    mos_dat["btt"][a] = True
 
        if evt.type == pg.MOUSEBUTTONUP:
            for a in range(3):
                if evt.button == a + 1:
                    mos_dat["btt"][a] = False
    
    mos_dat["chg"][0].append(mos_dat["xy"][1])

    if len(mos_dat["chg"][0]) > 2:
        mos_dat["chg"][0].pop(0)
    if len(mos_dat["chg"][0]) == 2:
        mos_dat["chg"][1] = (mos_dat["chg"][0][1] - mos_dat["chg"][0][0]) * -1

    if mos_dat["btt"][0] and bts.wrk_cur["cur"] == "viw" and bts.wrk_grp_s["viw"]["sld"] == 0:
        viw["scr"] -= mos_dat["chg"][1]

    scn["win"] = pg.transform.scale(scn["srf"], siz)
    scn["win-bck"] = pg.transform.scale(scn["srf"], siz)

    scn["win-bck"].set_alpha(51)

    dpy.blit(scn["win"], (0, 0))
    dpy.blit(scn["win-bck"], (scn["pix-siz"], scn["pix-siz"]))

    pg.display.update()
    pg.display.flip()
    fps.tick(0)