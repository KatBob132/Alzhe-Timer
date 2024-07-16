from scp.fnc import *

import pygame as pg

class txt_utl:
    def __init__(self, dat, srf):
        self.dat = jsn_dat(dat)
        self.srf = srf
    
    def siz(self, siz_txt, siz_siz, siz_sdw_plc=(0, 0)):
        self.siz_txt = str(siz_txt)
        self.siz_siz = int(siz_siz)
        self.siz_sdw_plc = (int(siz_sdw_plc[0]), int(siz_sdw_plc[1]))

        self.siz_ret = [0, 0]

        for a in range(len(self.siz_txt)):
            self.siz_ret[0] += len(self.dat[self.siz_txt[a]][0]) * self.siz_siz

            if a != len(self.siz_txt) - 1:
                self.siz_ret[0] += self.siz_siz
            else:
                self.siz_ret[0] += self.siz_sdw_plc[0]

            if (len(self.dat[self.siz_txt[a]]) + self.siz_sdw_plc[1]) * self.siz_siz > self.siz_ret[1]:
                self.siz_ret[1] = (len(self.dat[self.siz_txt[a]]) + self.siz_sdw_plc[1]) * self.siz_siz
            
        return self.siz_ret

    def drw(self, drw_txt, drw_xy, drw_siz, drw_clr, drw_sdw_plc=(0, 0), drw_sdw_clr=(0, 0, 0), drw_cnr=(False, False)):
        self.drw_txt = str(drw_txt)
        self.drw_xy = (int(drw_xy[0])), int(drw_xy[1])
        self.drw_siz = int(drw_siz)
        self.drw_clr = cfg_clr(drw_clr)

        self.drw_sdw_plc = (int(drw_sdw_plc[0]), int(drw_sdw_plc[1]))
        self.drw_sdw_clr = cfg_clr(drw_sdw_clr)

        self.drw_cnr = (bool(drw_cnr[0]), bool(drw_cnr[1]))
        self.drw_cnr_siz = self.siz(self.drw_txt, self.drw_siz, self.drw_sdw_plc)
        self.drw_cnr_add = [0, 0]

        for a in range(2):
            if self.drw_cnr[a]:
                self.drw_cnr_add[a] += -int(self.drw_cnr_siz[a] / 2)

        self.drw_plc = 0

        for let in self.drw_txt:
            for y in range(len(self.dat[let])):
                for x in range(len(self.dat[let][0])):
                    if self.dat[let][y][x] == 1:
                        if self.drw_sdw_plc != (0, 0):
                            pg.draw.rect(self.srf, self.drw_sdw_clr, pg.FRect(self.drw_xy[0] + self.drw_plc + (x * self.drw_siz) + (self.drw_sdw_plc[0] * self.drw_siz) + self.drw_cnr_add[0], self.drw_xy[1] + (y * self.drw_siz) + (self.drw_sdw_plc[1] * self.drw_siz) + self.drw_cnr_add[1], self.drw_siz, self.drw_siz))

                        pg.draw.rect(self.srf, self.drw_clr, pg.FRect(self.drw_xy[0] + self.drw_plc + (x * self.drw_siz) + self.drw_cnr_add[0], self.drw_xy[1] + (y * self.drw_siz) + self.drw_cnr_add[1], self.drw_siz, self.drw_siz))
            
            self.drw_plc += len(self.dat[let][0]) * self.drw_siz + self.drw_siz