from scp.fnc import *

import pygame.freetype as ftp

class fnt:
    def __init__(self, fnt_loc, fnt_srf):
        self.fnt_loc = str(fnt_loc)
        self.fnt_srf = fnt_srf

        ftp.init()
    
    def are(self, are_txt, are_siz, are_sdw_plc=(0, 0)):
        self.are_txt = str(are_txt)
        self.are_siz = int(are_siz)
        self.are_sdw_plc = (int(are_sdw_plc[0]), int(are_sdw_plc[1]))

        self.are_fnt = ftp.Font(self.fnt_loc, self.are_siz)
        self.are_s = (self.are_fnt.get_rect(self.are_txt).width + self.are_sdw_plc[0], self.are_fnt.get_rect(self.are_txt).height + self.are_sdw_plc[1])

        return self.are_s
        
    def drw(self, drw_txt, drw_xy, drw_siz, drw_clr, drw_sdw_plc=(0, 0), drw_sdw_clr=(0, 0, 0), drw_cnr=(False, False)):
        self.drw_txt = str(drw_txt)
        self.drw_xy = [int(drw_xy[0]), int(drw_xy[1])]
        self.drw_siz = int(drw_siz)
        self.drw_clr = cfg_clr(drw_clr)

        self.drw_sdw_plc = (int(drw_sdw_plc[0]), int(drw_sdw_plc[1]))
        self.drw_sdw_clr = cfg_clr(drw_sdw_clr)

        self.drw_cnr = (bool(drw_cnr[0]), bool(drw_cnr[1]))

        self.drw_fnt = ftp.Font(self.fnt_loc, self.drw_siz)
        self.drw_are = (self.drw_fnt.get_rect(self.drw_txt).width, self.drw_fnt.get_rect(self.drw_txt).height)

        for a in range(2):
            if self.drw_cnr[a]:
                self.drw_xy[a] -= self.drw_are[a] / 2
                self.drw_xy[a] = round(self.drw_xy[a])
        
        if self.drw_sdw_plc != (0, 0):
            self.drw_fnt = ftp.Font(self.fnt_loc, self.drw_siz)
            self.drw_fnt = self.drw_fnt.render(self.drw_txt, self.drw_sdw_clr)

            self.fnt_srf.blit(self.drw_fnt[0], (self.drw_xy[0] + self.drw_sdw_plc[0], self.drw_xy[1] + self.drw_sdw_plc[1]))

        self.drw_fnt = ftp.Font(self.fnt_loc, self.drw_siz)
        self.drw_fnt = self.drw_fnt.render(self.drw_txt, self.drw_clr)

        self.fnt_srf.blit(self.drw_fnt[0], self.drw_xy)