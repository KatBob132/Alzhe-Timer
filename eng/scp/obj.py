from re import T
from scp.utl import *
from scp.fnc import *

import pygame as pg

class wrk:
    def __init__(self, wrk_hst_clr, wrk_bck_clr, wrk_cer_clr, wrk_srf, wrk_lnk):
        self.wrk_hst_clr = cfg_clr(wrk_hst_clr)
        self.wrk_bck_clr = cfg_clr(wrk_bck_clr)
        self.wrk_cer_clr = cfg_clr(wrk_cer_clr)

        self.wrk_srf = wrk_srf
        self.wrk_lnk = wrk_lnk

        self.wrk_txt_siz = 22
        self.wrk_txt_spc = 2

        self.wrk_lrp = 0.2
        self.wrk_inc = 0.01

        self.wrk_grp_s = {}
        self.wrk_bts = {}
        self.wrk_cur = {}

        self.wrk_cur["cur"] = None
        self.wrk_cur["vis"] = None

    def add_grp(self, add_grp_nme, add_grp_shw=False):
        self.add_grp_nme = str(add_grp_nme)
        self.add_grp_shw = bool(add_grp_shw)

        self.wrk_bts[self.add_grp_nme] = {}
        
        self.wrk_grp_s[self.add_grp_nme] = {}
        self.wrk_grp_s[self.add_grp_nme]["shw"] = self.add_grp_shw

        if self.wrk_grp_s[self.add_grp_nme]["shw"]:
            self.wrk_grp_s[self.add_grp_nme]["sld"] = 0
        else:
            self.wrk_grp_s[self.add_grp_nme]["sld"] = 1
        
        if self.wrk_cur["cur"] == None:
            self.wrk_cur["cur"] = self.add_grp_nme
            self.wrk_cur["vis"] = self.add_grp_nme

    def add_bts(self, add_bts_grp, add_bts_txt, add_bts_xy, add_bts_cnr=(False, False)):
        self.add_bts_grp = str(add_bts_grp)
        self.add_bts_id = len(self.wrk_bts[self.add_grp_nme])

        self.add_bts_txt = str(add_bts_txt)
        self.add_bts_xy = [int(add_bts_xy[0]), int(add_bts_xy[1])]

        self.add_bts_siz = self.wrk_lnk.are(self.add_bts_txt, self.wrk_txt_siz, (0, self.wrk_txt_spc))
        self.add_bts_cnr = (bool(add_bts_cnr[0]), bool(add_bts_cnr[1]))

        for a in range(2):
            if self.add_bts_cnr[a]:
                self.add_bts_xy[a] -= self.add_bts_siz[a] / 2
                self.add_bts_xy[a] = round(self.add_bts_xy[a])
                self.add_bts_xy[a] -= self.wrk_txt_spc

        self.wrk_bts[self.add_bts_grp][self.add_bts_id] = {}

        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["txt"] = self.add_bts_txt
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["xy"] = self.add_bts_xy
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["siz"] = self.add_bts_siz
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["cls"] = self.wrk_bts[self.add_bts_grp][self.add_bts_id]["siz"][1] + self.wrk_txt_spc * 4
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["btt"] = 0

        if self.wrk_grp_s[self.add_bts_grp]["shw"]:
            self.wrk_bts[self.add_bts_grp][self.add_bts_id]["lrp"] = 0
        else:
            self.wrk_bts[self.add_bts_grp][self.add_bts_id]["lrp"] = 1
    
    def hov(self, hov_grp, hov_id, hov_xy):
        self.hov_grp = str(hov_grp)
        self.hov_id = int(hov_id)
        self.hov_xy = (int(hov_xy[0]), int(hov_xy[1]))

        self.hov_ing = False

        if self.wrk_grp_s[self.hov_grp]["shw"] and self.wrk_grp_s[self.hov_grp]["sld"] == 0:
            if self.hov_xy[0] >= self.wrk_bts[self.hov_grp][self.hov_id]["xy"][0] and self.hov_xy[0] <= self.wrk_bts[self.hov_grp][self.hov_id]["xy"][0] + self.wrk_bts[self.hov_grp][self.hov_id]["siz"][0]:
                if self.hov_xy[1] >= self.wrk_bts[self.hov_grp][self.hov_id]["xy"][1] and self.hov_xy[1] <= self.wrk_bts[self.hov_grp][self.hov_id]["xy"][1] + self.wrk_bts[self.hov_grp][self.hov_id]["siz"][1]:
                    self.hov_ing = True
        
        return self.hov_ing
    
    def bld(self, bld_grp, bld_id, bld_xy, bld_dlt):
        self.bld_grp = bld_grp
        self.bld_id = bld_id
        self.bld_xy = bld_xy
        self.bld_dlt = float(bld_dlt)

        if self.hov(self.bld_grp, self.bld_id, self.bld_xy):
            self.wrk_bts[self.bld_grp][self.bld_id]["lrp"] = lrp(self.wrk_bts[self.bld_grp][self.bld_id]["lrp"], 1, self.wrk_lrp, self.bld_dlt, self.wrk_inc)
        else:
            self.wrk_bts[self.bld_grp][self.bld_id]["lrp"] = lrp(self.wrk_bts[self.bld_grp][self.bld_id]["lrp"], 0, self.wrk_lrp, self.bld_dlt, self.wrk_inc)
    
    def fix(self, fix_xy, fix_btt, fix_dlt):
        self.fix_xy = fix_xy
        self.fix_dlt = fix_dlt
        self.fix_btt = bool(fix_btt)

        for grp in self.wrk_bts:
            for id in self.wrk_bts[grp]:
                self.bld(grp, id, self.fix_xy, self.fix_dlt)

                if self.hov(grp, id, self.fix_xy) and self.fix_btt:
                    self.wrk_bts[grp][id]["btt"] = 1
                else:
                    self.wrk_bts[grp][id]["btt"] = lrp(self.wrk_bts[grp][id]["btt"], 0, self.wrk_lrp, self.fix_dlt, self.wrk_inc)
    
    def chg(self, chg_dlt):
        self.chg_dlt = float(chg_dlt)

        if self.wrk_cur["vis"] != self.wrk_cur["cur"]:
            if self.wrk_grp_s[self.wrk_cur["vis"]]["shw"]:
                self.wrk_grp_s[self.wrk_cur["vis"]]["sld"] = lrp(self.wrk_grp_s[self.wrk_cur["vis"]]["sld"], 1, self.wrk_lrp, self.bld_dlt, self.wrk_inc)

                if self.wrk_grp_s[self.wrk_cur["vis"]]["sld"] == 1:
                    self.wrk_grp_s[self.wrk_cur["vis"]]["shw"] = False
                    self.wrk_grp_s[self.wrk_cur["cur"]]["shw"] = True
                    self.wrk_cur["vis"] = self.wrk_cur["cur"]
        else:
            if self.wrk_grp_s[self.wrk_cur["vis"]]["sld"] != 0:
                self.wrk_grp_s[self.wrk_cur["vis"]]["sld"] = lrp(self.wrk_grp_s[self.wrk_cur["vis"]]["sld"], 0, self.wrk_lrp, self.bld_dlt, self.wrk_inc)

    def drw(self):
        for grp in self.wrk_bts:
            if self.wrk_grp_s[grp]["shw"]:
                for id in self.wrk_bts[grp]:
                    pg.draw.rect(self.wrk_srf, self.wrk_hst_clr, pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1] + self.wrk_txt_spc, self.wrk_bts[grp][id]["siz"][0] + self.wrk_txt_spc * 2, self.wrk_bts[grp][id]["siz"][1] + self.wrk_txt_spc * 2))
                    pg.draw.rect(self.wrk_srf, bld_clr(self.wrk_bck_clr, self.wrk_cer_clr, self.wrk_bts[grp][id]["lrp"]), pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1], self.wrk_bts[grp][id]["siz"][0] + self.wrk_txt_spc * 2, self.wrk_bts[grp][id]["siz"][1] + self.wrk_txt_spc * 2))
                    pg.draw.rect(self.wrk_srf, bld_clr(bld_clr(self.wrk_bck_clr, self.wrk_cer_clr, self.wrk_bts[grp][id]["lrp"]), self.wrk_hst_clr, self.wrk_bts[grp][id]["btt"]), pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1], self.wrk_bts[grp][id]["siz"][0] + self.wrk_txt_spc * 2, self.wrk_bts[grp][id]["siz"][1] + self.wrk_txt_spc * 2), 1)

                    self.wrk_lnk.drw(self.wrk_bts[grp][id]["txt"], (self.wrk_bts[grp][id]["xy"][0] + self.wrk_txt_spc, self.wrk_bts[grp][id]["xy"][1] + self.wrk_txt_spc), self.wrk_txt_siz, self.wrk_hst_clr, (0, self.wrk_txt_spc), bld_clr(self.wrk_cer_clr, self.wrk_bck_clr, self.wrk_bts[grp][id]["lrp"]))

                    pg.draw.rect(self.wrk_srf, self.wrk_cer_clr, pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1], self.wrk_bts[grp][id]["siz"][0] + self.wrk_txt_spc * 2, self.wrk_bts[grp][id]["cls"] * self.wrk_grp_s[grp]["sld"]))
    
    def upt(self, upt_xy, upt_btt, upt_dlt):
        self.upt_xy = upt_xy
        self.upt_btt = upt_btt
        self.upt_dlt = upt_dlt

        self.chg(self.upt_dlt)
        self.fix(self.upt_xy, self.upt_btt, self.upt_dlt)
        self.drw()