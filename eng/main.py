from scp.obj import *
from scp.utl import *
from scp.fnc import *

from pygame.locals import *
import pygame as pg

from calendar import monthrange as mon
from datetime import datetime as dat
from time import time as tme
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

# Thought >
# Today >
# Everyday
# Faraway >
 
# View Reminders

hst_clr = clr["blue"]
bck_clr = clr["black"]
cer_clr = clr["white"]

ret = None

dte = {}

dte["now"] = dat.now()

dte["mon"] = dte["now"].month
dte["day"] = dte["now"].day
dte["yer"] = dte["now"].year

dte["hor"] = dte["now"].hour
dte["min"] = dte["now"].minute
dte["per"] = None

if dte["hor"] >= 12:
    dte["per"] = "PM"
    dte["hor"] -= 12
else:
    dte["per"] = "AM"

bts = wrk(hst_clr, bck_clr, cer_clr, scn["srf"], txt)

bts.add_grp("mnu")

bts.add_grp("tht")
bts.add_grp("tod")
bts.add_grp("evy", True)
bts.add_grp("far")

### Menu

bts.add_bts("mnu", "Thought", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 49), (True, True))
bts.add_bts("mnu", "Today", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 15), (True, True))
bts.add_bts("mnu", "Everyday", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 19), (True, True))
bts.add_bts("mnu", "Faraway", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 53), (True, True))

bts.add_icn("mnu", "Reminder's", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 82), (scn["siz"][0] // 2, scn["siz"][1] + 9), (True, True))

### Thought

bts.add_bts("tht", "Thought", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 32), (True, True))
bts.add_bts("tht", "Done", (scn["siz"][0] // 2, scn["siz"][1] // 2), (True, True))
bts.add_bts("tht", "Cancel", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 30), (True, True))

### Today

bts.add_bts("tod", "12", (scn["siz"][0] // 2 - 34, scn["siz"][1] // 2 - 43), (True, True))
bts.add_bts("tod", "59", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 43), (True, True))
bts.add_bts("tod", "AM", (scn["siz"][0] // 2 + 34, scn["siz"][1] // 2 - 43), (True, True))

bts.add_icn("tod", ":", (scn["siz"][0] // 2 - 17, scn["siz"][1] // 2 - 43), (-3, scn["siz"][1] // 2 - 43), (True, True))
bts.add_icn("tod", ":", (scn["siz"][0] // 2 + 17, scn["siz"][1] // 2 - 43), (scn["siz"][0] + 2, scn["siz"][1] // 2 - 43), (True, True))

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

bts.add_bts("evy", "12", (scn["siz"][0] // 2 - 34, scn["siz"][1] // 2), (True, True))
bts.add_bts("evy", "59", (scn["siz"][0] // 2, scn["siz"][1] // 2), (True, True))
bts.add_bts("evy", "AM", (scn["siz"][0] // 2 + 34, scn["siz"][1] // 2), (True, True))

bts.add_icn("evy", ":", (scn["siz"][0] // 2 - 17, scn["siz"][1] // 2), (-3, scn["siz"][1] // 2), (True, True))
bts.add_icn("evy", ":", (scn["siz"][0] // 2 + 17, scn["siz"][1] // 2), (scn["siz"][0] + 2, scn["siz"][1] // 2), (True, True))

bts.add_bts("evy", "Note", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 30), (True, True))
bts.add_bts("evy", "Done", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 60), (True, True))
bts.add_bts("evy", "Cancel", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 90), (True, True))

### Farawau

bts.add_bts("far", "12", (scn["siz"][0] // 2 - 34, scn["siz"][1] // 2 - 60), (True, True))
bts.add_bts("far", "12", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 60), (True, True))
bts.add_bts("far", "9999", (scn["siz"][0] // 2 + 47, scn["siz"][1] // 2 - 60), (True, True))

bts.add_icn("far", ":", (scn["siz"][0] // 2 - 17, scn["siz"][1] // 2 - 60), (-3, scn["siz"][1] // 2 - 60), (True, True))
bts.add_icn("far", ":", (scn["siz"][0] // 2 + 17, scn["siz"][1] // 2 - 60), (scn["siz"][0] + 2, scn["siz"][1] // 2 - 60), (True, True))

bts.add_bts("far", "12", (scn["siz"][0] // 2 - 34, scn["siz"][1] // 2 - 30), (True, True))
bts.add_bts("far", "59", (scn["siz"][0] // 2, scn["siz"][1] // 2 - 30), (True, True))
bts.add_bts("far", "AM", (scn["siz"][0] // 2 + 34, scn["siz"][1] // 2 - 30), (True, True))

bts.add_icn("far", ":", (scn["siz"][0] // 2 - 17, scn["siz"][1] // 2 - 30), (-3, scn["siz"][1] // 2 - 30), (True, True))
bts.add_icn("far", ":", (scn["siz"][0] // 2 + 17, scn["siz"][1] // 2 - 30), (scn["siz"][0] + 2, scn["siz"][1] // 2 - 30), (True, True))

bts.add_bts("far", "Note", (scn["siz"][0] // 2, scn["siz"][1] // 2), (True, True))
bts.add_bts("far", "Done", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 30), (True, True))
bts.add_bts("far", "Cancel", (scn["siz"][0] // 2, scn["siz"][1] // 2 + 60), (True, True))

pg.init()
dpy = pg.display.set_mode(siz, DOUBLEBUF)
pg.display.set_caption("Alzhe Timer")
fps = pg.time.Clock()

mos_dat = {}

mos_dat["xy"] = (pg.mouse.get_pos()[0] // scn["pix-siz"], pg.mouse.get_pos()[1] // scn["pix-siz"])
mos_dat["btt"] = [False, False, False]
mos_dat["clk"] = [tme(), 0]

key = {}

key["act"] = False
key["kys"] = ""

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
    dte["yer"] = dte["now"].year

    dte["hor"] = dte["now"].hour
    dte["min"] = dte["now"].minute
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

    ret = bts.upt(mos_dat["xy"], mos_dat["btt"][0], tme_cal["dlt"])

    mos_dat["clk"][1] = tme()

    if ret != None:
        mos_dat["btt"][0] = False
        mos_dat["clk"][0] = tme()

        match ret[0]:
            case "mnu":
                match ret[1]:
                    case 0:
                        key["kys"] = ""
                        
                        bts.chg_grp("tht")

                        bts.chg_bts("tht", 0, "Thought")
                    case 1:
                        key["kys"] = ""

                        bts.chg_grp("tod")

                        bts.chg_bts("tod", 0, dte["hor"])
                        bts.chg_bts("tod", 1, dte["min"])
                        bts.chg_bts("tod", 2, dte["per"])
                        bts.chg_bts("tod", 3, "Note")
                    case 2:
                        key["kys"] = ""

                        bts.chg_grp("evy")

                        for a in range(7):
                            bts.chg_bts("evy", a, "")
                        
                        bts.chg_bts("evy", 7, dte["hor"])
                        bts.chg_bts("evy", 8, dte["min"])
                        bts.chg_bts("evy", 9, dte["per"])
                        bts.chg_bts("evy", 10, "Note")
                    case 3:
                        key["kys"] = ""

                        bts.chg_grp("far")

                        bts.chg_bts("far", 0, dte["mon"])
                        bts.chg_bts("far", 1, dte["day"])
                        bts.chg_bts("far", 2, dte["yer"])
                        bts.chg_bts("far", 3, dte["hor"])
                        bts.chg_bts("far", 4, dte["min"])
                        bts.chg_bts("far", 5, dte["per"])
                        bts.chg_bts("far", 6, "Note")
            
            case "tht":
                match ret[1]:
                    case 0:
                        key["act"] = True
                        key["kys"] = ""
                    case 1:
                        bts.chg_grp("mnu")
                        key["act"] = False
                    case 2:
                        bts.chg_grp("mnu")
                        key["act"] = False
            
            case "tod":
                match ret[1]:
                    case 0:
                        bts.chg_num(ret[0], ret[1], 1, 12)
                    case 1:
                        bts.chg_num(ret[0], ret[1], 1, 59, True)
                    case 2:
                        if bts.get_bts(ret[0], ret[1]) == "AM":
                            bts.chg_bts(ret[0], ret[1], "PM")
                        else:
                            bts.chg_bts(ret[0], ret[1], "AM")
                    case 3:
                        key["act"] = True
                        key["kys"] = ""
                    case 4:
                        bts.chg_grp("mnu")
                        key["act"] = False
                    case 5:
                        bts.chg_grp("mnu")
                        key["act"] = False
            
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
                        bts.chg_num(ret[0], ret[1], 1, 12)
                    case 8:
                        bts.chg_num(ret[0], ret[1], 1, 59, True)
                    case 9:
                        if bts.get_bts(ret[0], ret[1]) == "AM":
                            bts.chg_bts(ret[0], ret[1], "PM")
                        else:
                            bts.chg_bts(ret[0], ret[1], "AM")
                    case 10:
                        key["act"] = True  
                        key["kys"] = ""
                    case 11:
                        bts.chg_grp("mnu")
                        key["act"] = False
                    case 12:
                        bts.chg_grp("mnu")
                        key["act"] = False

            case "far":
                match ret[1]:
                    case 0:
                        bts.chg_num(ret[0], ret[1], 1, 12)
                    case 1:
                        bts.chg_num(ret[0], ret[1], 1, mon(int(bts.get_bts("far", 2)), int(bts.get_bts("far", 0)))[1])
                    case 2:
                        bts.chg_num(ret[0], ret[1], 1, 9999)
                    case 3:
                        bts.chg_num(ret[0], ret[1], 1, 12)
                    case 4:
                        bts.chg_num(ret[0], ret[1], 1, 59, True)
                    case 5:
                        if bts.get_bts(ret[0], ret[1]) == "AM":
                            bts.chg_bts(ret[0], ret[1], "PM")
                        else:
                            bts.chg_bts(ret[0], ret[1], "AM")
                    case 6:
                        key["act"] = True  
                        key["kys"] = ""
                    case 7:
                        bts.chg_grp("mnu")
                        key["act"] = False
                    case 8:
                        bts.chg_grp("mnu")
                        key["act"] = False

    pg.draw.rect(scn["srf"], clr["green"], pg.Rect(mos_dat["xy"][0] - 3, mos_dat["xy"][1] - 3, 6, 6))

    txt.drw("Alzhe Timer", (scn["siz"][0] // 2, 2), 26, hst_clr, (0, 2), bck_clr, (True, False))

    if key["act"]:
        match bts.get_grp():
            case "tht":
                bts.chg_hgh(bts.get_grp(), 0, True)
                bts.chg_bts(bts.get_grp(), 0, key["kys"])
            case "tod":
                bts.chg_hgh(bts.get_grp(), 3, True)
                bts.chg_bts(bts.get_grp(), 3, key["kys"])                
            case "evy":
                bts.chg_hgh(bts.get_grp(), 10, True)
                bts.chg_bts(bts.get_grp(), 10, key["kys"])
            case "far":
                bts.chg_hgh(bts.get_grp(), 6, True)
                bts.chg_bts(bts.get_grp(), 6, key["kys"])
    else:
        bts.chg_hgh("tht", 0, False)
        bts.chg_hgh("tod", 3, False)
        bts.chg_hgh("evy", 10, False)
        bts.chg_hgh("far", 6, False)
    
    for evt in pg.event.get():
        if evt.type == pg.QUIT:
            pg.quit()
            ext()

        if evt.type == pg.KEYDOWN:
            if key["act"]:
                key["kys"] += evt.unicode

                if evt.key == pg.K_BACKSPACE:
                    key["kys"] = key["kys"][:-2]
                if evt.key == pg.K_RETURN:
                    key["act"] = False
                    key["kys"] = key["kys"][:-1]
                
                match bts.get_grp():
                    case "tht":
                        bts.chg_clk(bts.get_grp(), 0)
                    case "tod":
                        bts.chg_clk(bts.get_grp(), 3)
                    case "evy":
                        bts.chg_clk(bts.get_grp(), 10)
                    case "far":
                        bts.chg_clk(bts.get_grp(), 6)
                
            if evt.key == pg.K_ESCAPE:
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
    
    scn["win"] = pg.transform.scale(scn["srf"], siz)
    scn["win-bck"] = pg.transform.scale(scn["srf"], siz)

    scn["win-bck"].set_alpha(51)

    dpy.blit(scn["win"], (0, 0))
    dpy.blit(scn["win-bck"], (scn["pix-siz"], scn["pix-siz"]))

    pg.display.update()
    pg.display.flip()
    fps.tick(0)