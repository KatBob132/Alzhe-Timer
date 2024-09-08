from scp.obj import *
from scp.utl import *
from scp.fnc import *

from pygame.locals import *
import pygame as pg

from calendar import monthrange as mon
from time import time as tme
from sys import exit as ext

clr = jsn_dat("eng/dat/clr.json")
scn = {}

scn["siz"] = (256, 256)
scn["pix-siz"] = 4

scn["srf"] = pg.Surface(scn["siz"])

scn["win"] = None
scn["win-bck"] = None

siz = (scn["siz"][0] * scn["pix-siz"], scn["siz"][1] * scn["pix-siz"])
txt = txt_utl("eng/dat/fnt.json", scn["srf"])

tme_cal = {}
fps_cal = {}

tme_cal["str"] = tme()
tme_cal["now"] = 0
tme_cal["dlt"] = 0

fps_cal["fps"] = 0
fps_cal["fps-lit"] = []
fps_cal["fps-avg"] = 0

# Faraway Alarm
# Today Alarm
# Daily Alarm
# View Alarms

hst_clr = clr["red"]
bck_clr = clr["white"]
clr_clr = clr["black"]

bts = v_wrk(bck_clr, clr_clr, hst_clr, txt, scn["srf"], scn["siz"])

bts.add_grp("mnu")
bts.add_grp("mnu-2", False)

bts.add_bts("mnu", (128, 102), "1", (True, True))
bts.add_bts("mnu", (128, 128), "2", (True, True))
bts.add_bts("mnu", (128, 154), "3", (True, True))

bts.add_bts("mnu-2", (128, 102), "1", (True, True))
bts.add_bts("mnu-2", (128, 128), "2", (True, True))
bts.add_bts("mnu-2", (128, 154), "x", (True, True))

pg.init()
dpy = pg.display.set_mode(siz, DOUBLEBUF)
pg.display.set_caption("Alzhe Timer")
fps = pg.time.Clock()

mos_dat = {}

mos_dat["xy"] = (pg.mouse.get_pos()[0] // scn["pix-siz"], pg.mouse.get_pos()[1] // scn["pix-siz"])
mos_dat["btt"] = [False, False, False]

while True:
    dpy.fill(clr_clr)
    scn["srf"].fill(clr_clr)

    # pg.mouse.set_visible(False)

    mos_dat["xy"] = (pg.mouse.get_pos()[0] // scn["pix-siz"], pg.mouse.get_pos()[1] // scn["pix-siz"])

    tme_cal["now"] = tme()
    tme_cal["dlt"] = (tme_cal["now"] - tme_cal["str"])
    tme_cal["str"] = tme()

    fps_cal["fps"] = 1 / tme_cal["dlt"]
    fps_cal["fps-lit"].append(fps_cal["fps"])

    while len(fps_cal["fps-lit"]) > round(fps_cal["fps"]):
        fps_cal["fps-lit"].pop(0)

    try:
        fps_cal["fps-avg"] = round(sum(fps_cal["fps-lit"]) / len(fps_cal["fps-lit"]))
    except:
        fps_cal["fps-avg"] = round(fps_cal["fps"])

    mos_dat["btt"][0] = bts.upt(tme_cal["dlt"], mos_dat["xy"], mos_dat["btt"][0])

    match bts.v_mos["grp"]:
        case "mnu":
            match bts.v_mos["id"]:
                case 0:
                    bts.chg_grp("mnu-2")
                case 1:
                    pass
                case 2:
                    pass

        case "mnu-2":
            match bts.v_mos["id"]:
                case 0:
                    bts.chg_num("mnu-2", 0, 1)
                case 1:
                    bts.chg_grp("mnu")
                case 2:
                    bts.chg_grp("mnu")

    pg.draw.rect(scn["srf"], clr["green"], pg.Rect(mos_dat["xy"][0], mos_dat["xy"][1], 2, 2))

    for evt in pg.event.get():
        if evt.type == pg.QUIT:
            pg.quit()
            ext()

        if evt.type == pg.KEYDOWN:
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