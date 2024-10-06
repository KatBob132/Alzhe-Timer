from re import T
from scp.obj import *
from scp.utl import *
from scp.fnc import *

from pygame.locals import *
import pygame as pg

from calendar import monthrange as mon
from time import time as tme
from sys import exit as ext

scn = {}

scn["siz"] = (384, 384)
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

# Faraway Alarm
# Today Alarm
# Daily Alarm
# View Alarms

hst_clr = clr["red"]
bck_clr = clr["black"]
cer_clr = clr["white"]

bts = wrk(hst_clr, bck_clr, cer_clr, scn["srf"], txt)

bts.add_grp("mnu", True)
bts.add_grp("far")

bts.add_bts("mnu", "Faraway", (192, 192), (True, True))

bts.add_bts("far", "123", (192, 192), (True, True))

pg.init()
dpy = pg.display.set_mode(siz, DOUBLEBUF)
pg.display.set_caption("Alzhe Timer")
fps = pg.time.Clock()

mos_dat = {}

mos_dat["xy"] = (pg.mouse.get_pos()[0] // scn["pix-siz"], pg.mouse.get_pos()[1] // scn["pix-siz"])
mos_dat["btt"] = [False, False, False]

while True:
    dpy.fill(cer_clr)
    scn["srf"].fill(cer_clr)

    mos_dat["xy"] = (pg.mouse.get_pos()[0] // scn["pix-siz"], pg.mouse.get_pos()[1] // scn["pix-siz"])

    tme_cal["now"] = tme()
    tme_cal["dlt"] = (tme_cal["now"] - tme_cal["str"])
    tme_cal["str"] = tme()

    fps_cal["fps"] = 1 / tme_cal["dlt"]
    fps_cal["fps-lit"].append(fps_cal["fps"])

    if len(fps_cal["fps-lit"]) > round(fps_cal["fps"]):
        fps_cal["fps-lit"].pop(0)

    fps_cal["fps-avg"] = round(sum(fps_cal["fps-lit"]) / len(fps_cal["fps-lit"]))
    
    bts.upt(mos_dat["xy"], mos_dat["btt"][0], tme_cal["dlt"])

    txt.drw("Alzhe Timer", (192, 2), 26, hst_clr, (0, 2), clr["black"], (True, False))
    
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