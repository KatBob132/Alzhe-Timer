from scp.obj import *
from scp.utl import *
from scp.fnc import *

from pygame.locals import *
import pygame as pg

from time import time as tme
from sys import exit as ext

clr = jsn_dat("eng/dat/clr.json")
scn = {}

scn["siz"] = (256, 256)
scn["pix-siz"] = 3

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

# red green blue orange pink
chc_clr = clr["red"]
bck_clr = clr["white"]
for_clr = clr["black"]

# Faraway Alarm
# Today Alarm
# Daily Alarm
# View Alarms

btt = btt_obj(chc_clr, bck_clr, for_clr, 0.2, 0.2, scn["srf"], txt, 2, "menu")

btt.add_grp("menu")
btt.add_grp("faraway")
# btt.add_grp("today")
# btt.add_grp("daily")
# btt.add_grp("view")

btt.add_btt("menu", "Faraway", (128, 128 - 41), (True, True))
btt.add_btt("menu", "Today", (128, 128 - 14), (True, True))
btt.add_btt("menu", "Daily", (128, 128 + 13), (True, True))
btt.add_btt("menu", "View", (128, 128 + 38), (True, True))

btt.add_btt("faraway", "5", (128, 128 - 41), (True, True))
btt.add_btt("faraway", "4", (128, 128 - 14), (True, True))
btt.add_btt("faraway", "3", (128, 128 + 13), (True, True))
btt.add_btt("faraway", "1", (128, 128 + 38), (True, True))

pg.init()
dpy = pg.display.set_mode(siz, DOUBLEBUF)
pg.display.set_caption("Alzhe Timer")
fps = pg.time.Clock()

mos_dat = {}

mos_dat["xy"] = (pg.mouse.get_pos()[0] // scn["pix-siz"], pg.mouse.get_pos()[1] // scn["pix-siz"])
mos_dat["btt"] = [False, False, False]

while True:
    dpy.fill(bck_clr)
    scn["srf"].fill(bck_clr)

    pg.mouse.set_visible(False)

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
        fps_cal["fps-avg"] = round(fps_cal["fps "])

    # pg.draw.rect(scn["srf"], clr["green"], pg.Rect(scn["siz"][0] / 2, 0, 1, scn["siz"][1]))
    # pg.draw.rect(scn["srf"], clr["green"], pg.Rect(0, scn["siz"][1] / 2, scn["siz"][0], 1))

    btt.upt(tme_cal["dlt"], mos_dat["xy"])

    pg.draw.rect(scn["srf"], clr["green"], pg.Rect(mos_dat["xy"][0] - 1, mos_dat["xy"][1] - 1, 3, 3))

    txt.drw("Alzhe", (2, 2), 3, chc_clr, (0, 1), for_clr)
    txt.drw("Timer", (2, 26), 3, for_clr, (0, 1), chc_clr)

    for evt in pg.event.get():
        if evt.type == pg.QUIT:
            pg.quit()
            ext()

        if evt.type == pg.KEYDOWN:
            if evt.key == pg.K_ESCAPE:
                pg.quit()
                ext()
            
            if evt.key == pg.K_SPACE:
                upt = not upt

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