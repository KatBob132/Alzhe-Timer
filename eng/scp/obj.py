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

        tot_lrp = 0.2
        tot_inc = 0.0075

        self.wrk_grp_s = {}
        self.wrk_bts = {}
        self.wrk_icn = {}
        self.wrk_cur = {}

        self.wrk_cur["cur"] = None
        self.wrk_cur["vis"] = None

    def add_grp(self, add_grp_nme, add_grp_shw=False):
        self.add_grp_nme = str(add_grp_nme)
        self.add_grp_shw = bool(add_grp_shw)

        self.wrk_bts[self.add_grp_nme] = {}
        self.wrk_icn[self.add_grp_nme] = {}

        self.wrk_grp_s[self.add_grp_nme] = {}
        self.wrk_grp_s[self.add_grp_nme]["shw"] = self.add_grp_shw

        if self.wrk_grp_s[self.add_grp_nme]["shw"]:
            self.wrk_grp_s[self.add_grp_nme]["sld"] = 0
        else:
            self.wrk_grp_s[self.add_grp_nme]["sld"] = 1
        
        if self.wrk_cur["cur"] == None and add_grp_shw:
            self.wrk_cur["cur"] = self.add_grp_nme
            self.wrk_cur["vis"] = self.add_grp_nme
    
    def get_grp(self):
        return self.wrk_cur["cur"]
    
    def chg_grp(self, chg_grp_new):
        self.chg_grp_new = str(chg_grp_new)

        self.wrk_cur["cur"] = chg_grp_new

    def add_bts(self, add_bts_grp, add_bts_txt, add_bts_xy, add_bts_cnr=(False, False), add_bts_num=False):
        self.add_bts_grp = str(add_bts_grp)
        self.add_bts_id = len(self.wrk_bts[self.add_bts_grp])

        self.add_bts_txt = str(add_bts_txt)
        self.add_bts_xy = [int(add_bts_xy[0] + 1), int(add_bts_xy[1])]
        self.add_bts_org = (int(add_bts_xy[0] + 1), int(add_bts_xy[1]))

        self.add_bts_siz = self.wrk_lnk.are(self.add_bts_txt, self.wrk_txt_siz, (0, self.wrk_txt_spc))
        self.add_bts_siz = (self.add_bts_siz[0] + self.wrk_txt_spc * 2, self.add_bts_siz[1] + self.wrk_txt_spc * 2)
        self.add_bts_cnr = (bool(add_bts_cnr[0]), bool(add_bts_cnr[1]))

        for a in range(2):
            if self.add_bts_cnr[a]:
                self.add_bts_xy[a] -= self.add_bts_siz[a] / 2
                self.add_bts_xy[a] = round(self.add_bts_xy[a])

        self.add_bts_xy[1] -= self.wrk_txt_spc
        self.add_bts_num = bool(add_bts_num)

        self.wrk_bts[self.add_bts_grp][self.add_bts_id] = {}

        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["txt"] = self.add_bts_txt
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["xy"] = self.add_bts_xy
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["num"] = self.add_bts_num
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["siz"] = self.add_bts_siz
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["cnr"] = self.add_bts_cnr
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["org"] = self.add_bts_org
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["cls"] = self.wrk_bts[self.add_bts_grp][self.add_bts_id]["siz"][1] + self.wrk_txt_spc
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["btt"] = 0
        self.wrk_bts[self.add_bts_grp][self.add_bts_id]["hgh"] = False

        if self.wrk_grp_s[self.add_bts_grp]["shw"]:
            self.wrk_bts[self.add_bts_grp][self.add_bts_id]["lrp"] = 0
        else:
            self.wrk_bts[self.add_bts_grp][self.add_bts_id]["lrp"] = 1
    
    def get_bts(self, get_bts_grp, get_bts_id):
        self.get_bts_grp = str(get_bts_grp)
        self.get_bts_id = int(get_bts_id)

        return self.wrk_bts[self.get_bts_grp][self.get_bts_id]["txt"]
    
    def get_num(self, get_num_grp, get_num_id):
        self.get_num_grp = str(get_num_grp)
        self.get_num_id = int(get_num_id)
        
        return self.wrk_bts[self.get_num_grp][self.get_num_id]["num"]

    def chg_bts(self, chg_bts_grp, chg_bts_id, chg_bts_new):
        self.chg_bts_grp = str(chg_bts_grp)
        self.chg_bts_id = int(chg_bts_id)
        self.chg_bts_new = str(chg_bts_new)

        self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["txt"] = self.chg_bts_new
        self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["siz"] = self.wrk_lnk.are(self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["txt"], self.wrk_txt_siz, (0, self.wrk_txt_spc))
        self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["siz"] = (self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["siz"][0] + self.wrk_txt_spc * 2, self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["siz"][1] + self.wrk_txt_spc * 2)
        self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["cls"] = self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["siz"][1] + self.wrk_txt_spc

        for a in range(2):
            self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["xy"][a] = self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["org"][a]

            if self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["cnr"][a]:
                self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["xy"][a] -= self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["siz"][a] / 2
                self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["xy"][a] = round(self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["xy"][a])
        
        self.wrk_bts[self.chg_bts_grp][self.chg_bts_id]["xy"][1] -= self.wrk_txt_spc

    def chg_num(self, chg_num_grp, chg_num_id, chg_num_amt, chg_num_lim=-1, chg_num_min=0, chg_num_zer=False):
        self.chg_num_grp = chg_num_grp
        self.chg_num_id = chg_num_id
        self.chg_num_amt = int(chg_num_amt)

        self.chg_num_lim = int(chg_num_lim)
        self.chg_num_min = int(chg_num_min)
        self.chg_num_zer = bool(chg_num_zer)

        if self.chg_num_lim != -1:
            self.chg_num_new = str(whl(int(self.wrk_bts[self.chg_num_grp][self.chg_num_id]["txt"]) + self.chg_num_amt, self.chg_num_lim, self.chg_num_min, self.chg_num_zer))
        else:
            self.chg_num_new = str(int(self.wrk_bts[self.chg_num_grp][self.chg_num_id]["txt"]) + self.chg_num_amt)

        self.chg_bts(self.chg_num_grp, self.chg_num_id, self.chg_num_new)

    def chg_clk(self, chg_clk_grp, chg_clk_id):
        self.chg_clk_grp = str(chg_clk_grp)
        self.chg_clk_id = int(chg_clk_id)

        self.wrk_bts[self.chg_clk_grp][self.chg_clk_id]["btt"] = 1

    def chg_hgh(self, chg_hgh_grp, chg_hgh_id, chg_hgh_bol):
        self.chg_hgh_grp = str(chg_hgh_grp)
        self.chg_hgh_id = int(chg_hgh_id)
        self.chg_hgh_bol = bool(chg_hgh_bol)

        self.wrk_bts[self.chg_hgh_grp][self.chg_hgh_id]["hgh"] = self.chg_hgh_bol
    
    def add_icn(self, add_icn_grp, add_icn_txt, add_icn_xy, add_icn_dst, add_icn_cnr=(False, False)):
        self.add_icn_grp = str(add_icn_grp)
        self.add_icn_id = len(self.wrk_icn[self.add_icn_grp])

        self.add_icn_txt = str(add_icn_txt)
        self.add_icn_xy = [int(add_icn_xy[0]) + 1, int(add_icn_xy[1])]
        self.add_icn_dst = [int(add_icn_dst[0]), int(add_icn_dst[1])]
        self.add_icn_cnr = (bool(add_icn_cnr[0])), bool(add_icn_cnr[1])

        self.add_icn_siz = self.wrk_lnk.are(self.add_icn_txt, self.wrk_txt_siz, (0, self.wrk_txt_spc))

        for a in range(2):
            if self.add_icn_cnr[a]:
                self.add_icn_xy[a] -= self.add_icn_siz[a] / 2
                self.add_icn_xy[a] = round(self.add_icn_xy[a])

                self.add_icn_dst[a] -= self.add_icn_siz[a] / 2
                self.add_icn_dst[a] = round(self.add_icn_dst[a])

        self.wrk_icn[self.add_icn_grp][self.add_icn_id] = {}

        self.wrk_icn[self.add_icn_grp][self.add_icn_id]["txt"] = self.add_icn_txt
        self.wrk_icn[self.add_icn_grp][self.add_icn_id]["xy"] = self.add_icn_xy
        self.wrk_icn[self.add_icn_grp][self.add_icn_id]["dst"] = self.add_icn_dst
        self.wrk_icn[self.add_icn_grp][self.add_icn_id]["yus"] = [self.add_icn_xy[0], self.add_icn_xy[1]]
    
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
        self.bld_grp = str(bld_grp)
        self.bld_id = int(bld_id)
        self.bld_dlt = float(bld_dlt)
        self.bld_xy = bld_xy

        if self.hov(self.bld_grp, self.bld_id, self.bld_xy) or self.wrk_bts[self.bld_grp][self.bld_id]["hgh"]:
            self.wrk_bts[self.bld_grp][self.bld_id]["lrp"] = lrp(self.wrk_bts[self.bld_grp][self.bld_id]["lrp"], 1, tot_lrp, self.bld_dlt, tot_inc)
        else:
            self.wrk_bts[self.bld_grp][self.bld_id]["lrp"] = lrp(self.wrk_bts[self.bld_grp][self.bld_id]["lrp"], 0, tot_lrp, self.bld_dlt, tot_inc)
    
    def fix(self, fix_xy, fix_btt, fix_dlt):
        self.fix_xy = fix_xy
        self.fix_dlt = fix_dlt
        self.fix_btt = bool(fix_btt)

        self.fix_btt_dat = None

        for grp in self.wrk_bts:
            for id in self.wrk_bts[grp]:
                self.bld(grp, id, self.fix_xy, self.fix_dlt)

                if self.hov(grp, id, self.fix_xy) and self.fix_btt:
                    self.wrk_bts[grp][id]["btt"] = 1
                    self.fix_btt_dat = (grp, id)
                else:
                    self.wrk_bts[grp][id]["btt"] = lrp(self.wrk_bts[grp][id]["btt"], 0, tot_lrp, self.fix_dlt, tot_inc)
        
        return self.fix_btt_dat
    
    def chg(self, chg_dlt):
        self.chg_dlt = float(chg_dlt)

        if self.wrk_cur["vis"] != self.wrk_cur["cur"]:
            if self.wrk_grp_s[self.wrk_cur["vis"]]["shw"]:
                self.wrk_grp_s[self.wrk_cur["vis"]]["sld"] = lrp(self.wrk_grp_s[self.wrk_cur["vis"]]["sld"], 1, tot_lrp, self.bld_dlt, tot_inc)

                if self.wrk_grp_s[self.wrk_cur["vis"]]["sld"] == 1:
                    self.wrk_grp_s[self.wrk_cur["vis"]]["shw"] = False
                    self.wrk_grp_s[self.wrk_cur["cur"]]["shw"] = True
                    self.wrk_cur["vis"] = self.wrk_cur["cur"]
        else:
            if self.wrk_grp_s[self.wrk_cur["vis"]]["sld"] != 0:
                self.wrk_grp_s[self.wrk_cur["vis"]]["sld"] = lrp(self.wrk_grp_s[self.wrk_cur["vis"]]["sld"], 0, tot_lrp, self.bld_dlt, tot_inc)

    def drw(self):
        for grp in self.wrk_bts:
            if self.wrk_grp_s[grp]["shw"]:
                for id in self.wrk_bts[grp]:
                    pg.draw.rect(self.wrk_srf, self.wrk_hst_clr, pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1] + self.wrk_txt_spc, self.wrk_bts[grp][id]["siz"][0], self.wrk_bts[grp][id]["siz"][1]))
                    pg.draw.rect(self.wrk_srf, bld_clr(self.wrk_bck_clr, self.wrk_cer_clr, self.wrk_bts[grp][id]["lrp"]), pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1], self.wrk_bts[grp][id]["siz"][0], self.wrk_bts[grp][id]["siz"][1]))
                    pg.draw.rect(self.wrk_srf, bld_clr(bld_clr(self.wrk_bck_clr, self.wrk_cer_clr, self.wrk_bts[grp][id]["lrp"]), self.wrk_hst_clr, self.wrk_bts[grp][id]["btt"]), pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1], self.wrk_bts[grp][id]["siz"][0], self.wrk_bts[grp][id]["siz"][1]), 1)

                    self.wrk_lnk.drw(self.wrk_bts[grp][id]["txt"], (self.wrk_bts[grp][id]["xy"][0] + self.wrk_txt_spc, self.wrk_bts[grp][id]["xy"][1] + self.wrk_txt_spc), self.wrk_txt_siz, self.wrk_hst_clr, (0, self.wrk_txt_spc), bld_clr(self.wrk_cer_clr, self.wrk_bck_clr, self.wrk_bts[grp][id]["lrp"]))

                    pg.draw.rect(self.wrk_srf, self.wrk_cer_clr, pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1], self.wrk_bts[grp][id]["siz"][0], self.wrk_bts[grp][id]["cls"] * self.wrk_grp_s[grp]["sld"]))

                    pg.draw.rect(self.wrk_srf, self.wrk_cer_clr, pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1], 1, 1))
                    pg.draw.rect(self.wrk_srf, self.wrk_cer_clr, pg.Rect(self.wrk_bts[grp][id]["xy"][0] + self.wrk_bts[grp][id]["siz"][0] - 1, self.wrk_bts[grp][id]["xy"][1], 1, 1))
                    pg.draw.rect(self.wrk_srf, self.wrk_cer_clr, pg.Rect(self.wrk_bts[grp][id]["xy"][0], self.wrk_bts[grp][id]["xy"][1] + self.wrk_bts[grp][id]["cls"] - 1, 1, 1))
                    pg.draw.rect(self.wrk_srf, self.wrk_cer_clr, pg.Rect(self.wrk_bts[grp][id]["xy"][0] + self.wrk_bts[grp][id]["siz"][0] - 1, self.wrk_bts[grp][id]["xy"][1] + self.wrk_bts[grp][id]["cls"] - 1, 1, 1))
                
                for icn in self.wrk_icn[grp]:
                    for a in range(2):
                        self.wrk_icn[grp][icn]["yus"][a] = self.wrk_icn[grp][icn]["xy"][a] + (self.wrk_icn[grp][icn]["dst"][a] - self.wrk_icn[grp][icn]["xy"][a]) * self.wrk_grp_s[grp]["sld"]
                    
                    self.wrk_lnk.drw(self.wrk_icn[grp][icn]["txt"], self.wrk_icn[grp][icn]["yus"], self.wrk_txt_siz, self.wrk_hst_clr, (0, self.wrk_txt_spc), self.wrk_bck_clr)


    def upt(self, upt_xy, upt_btt, upt_dlt):
        self.upt_xy = upt_xy
        self.upt_btt = upt_btt
        self.upt_dlt = upt_dlt

        self.chg(self.upt_dlt)
        self.drw()

        return self.fix(self.upt_xy, self.upt_btt, self.upt_dlt)