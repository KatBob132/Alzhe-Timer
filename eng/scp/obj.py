from scp.utl import *
from scp.fnc import *

class v_wrk:
    def __init__(self, v_clr, v_hov_clr, v_txt_clr, v_lnk, v_srf, v_scn):
        self.v_clr = cfg_clr(v_clr)
        self.v_hov_clr = cfg_clr(v_hov_clr)
        self.v_txt_clr = cfg_clr(v_txt_clr)

        self.v_lnk = v_lnk

        self.v_srf = v_srf
        self.v_scn = (int(v_scn[0]), int(v_scn[1]))

        self.v_siz = 2
        self.v_lrp = 0.2
        self.v_inc = 0.01
        
        self.v_bts = {}
        self.v_set = {}
        
        self.v_cur = {}

        self.v_cur["grp"] = None
        self.v_cur["grp-vis"] = None

        self.v_mos = {}
        
        self.v_mos["grp"] = None
        self.v_mos["id"] = None
         
    def add_grp(self, add_grp_nme, add_grp_shw=True):
        self.add_grp_nme = str(add_grp_nme)
        self.add_grp_shw = bool(add_grp_shw)

        self.v_bts[self.add_grp_nme] = {}
        self.v_set[self.add_grp_nme] = {}
 
        self.v_set[self.add_grp_nme]["shw"] = self.add_grp_shw

        if self.add_grp_shw:
            self.v_set[self.add_grp_nme]["phs"] = 1
        else:
            self.v_set[self.add_grp_nme]["phs"] = 0
        
        if len(self.v_set) == 1:
            self.v_cur["grp"] = self.add_grp_nme
            self.v_cur["grp-vis"] = self.add_grp_nme

    def add_bts(self, add_bts_grp, add_bts_xy, add_bts_num, add_bts_cnr=(False, False)):
        self.add_bts_grp = str(add_bts_grp)
        self.add_bts_id = len(self.v_bts[self.add_bts_grp])

        self.add_bts_xy = (int(add_bts_xy[0]), int(add_bts_xy[1]))
        self.add_bts_org = (int(add_bts_xy[0]), int(add_bts_xy[1]))
        
        self.add_bts_num = str(add_bts_num)
        self.add_bts_cnr = (bool(add_bts_cnr[0]), bool(add_bts_cnr[1]))

        self.add_bts_siz = self.v_lnk.siz(self.add_bts_num, self.v_siz, (0, 1))

        self.v_bts[self.add_bts_grp][self.add_bts_id] = {}

        self.v_bts[self.add_bts_grp][self.add_bts_id]["num"] = self.add_bts_num

        self.v_bts[self.add_bts_grp][self.add_bts_id]["xy"] = [self.add_bts_xy[0], self.add_bts_xy[1]]
        self.v_bts[self.add_bts_grp][self.add_bts_id]["org"] = (self.add_bts_org[0], self.add_bts_org[1])
        self.v_bts[self.add_bts_grp][self.add_bts_id]["cnr"] = (self.add_bts_cnr[0], self.add_bts_cnr[1])

        self.v_bts[self.add_bts_grp][self.add_bts_id]["siz"] = (self.add_bts_siz[0] + self.v_siz * 2, self.add_bts_siz[1] + self.v_siz * 2)
        self.v_bts[self.add_bts_grp][self.add_bts_id]["hov"] = 0
        self.v_bts[self.add_bts_grp][self.add_bts_id]["fil"] = self.v_bts[self.add_bts_grp][self.add_bts_id]["siz"][1] + self.v_siz
        self.v_bts[self.add_bts_grp][self.add_bts_id]["clk"] = 0

        for a in range(2):
            if self.add_bts_cnr[a]:
                self.v_bts[self.add_bts_grp][self.add_bts_id]["xy"][a] -= self.v_bts[self.add_bts_grp][self.add_bts_id]["siz"][a] // 2
    
    def chg_grp(self, chg_grp_new):
        self.chg_grp_new = str(chg_grp_new)
        self.v_cur["grp"] = self.chg_grp_new
    
    def chg_num(self, chg_num_grp, chg_num_id, chg_num_amt):
        self.chg_num_grp = str(chg_num_grp)
        self.chg_num_id = int(chg_num_id)
        self.chg_num_amt = int(chg_num_amt)
        
        self.v_bts[self.chg_num_grp][self.chg_num_id]["num"] = str(int(self.v_bts[self.chg_num_grp][self.chg_num_id]["num"]) + self.chg_num_amt)
        self.chg_num_siz = self.v_lnk.siz(self.v_bts[self.chg_num_grp][self.chg_num_id]["num"], self.v_siz, (0, 1))

        self.v_bts[self.chg_num_grp][self.chg_num_id]["siz"] = (self.chg_num_siz[0] + self.v_siz * 2, self.chg_num_siz[1] + self.v_siz * 2)
        self.v_bts[self.chg_num_grp][self.chg_num_id]["xy"] = [self.v_bts[self.chg_num_grp][self.chg_num_id]["org"][0], self.v_bts[self.chg_num_grp][self.chg_num_id]["org"][1]]

        for a in range(2):
            if self.v_bts[self.chg_num_grp][self.chg_num_id]["cnr"][a]:
                self.v_bts[self.chg_num_grp][self.chg_num_id]["xy"][a] -= int(self.v_bts[self.chg_num_grp][self.chg_num_id]["siz"][a] / 2)

    def hov(self, hov_grp, hov_id, hov_mos):
        self.hov_grp = str(hov_grp)
        self.hov_id = int(hov_id)

        self.hov_mos = (int(hov_mos[0]), int(hov_mos[1]))
        self.hov_d = False

        if self.hov_mos[0] >= self.v_bts[self.hov_grp][self.hov_id]["xy"][0] and self.hov_mos[0] <= self.v_bts[self.hov_grp][self.hov_id]["xy"][0] + self.v_bts[self.hov_grp][self.hov_id]["siz"][0]:
            if self.hov_mos[1] >= self.v_bts[self.hov_grp][self.hov_id]["xy"][1] and self.hov_mos[1] <= self.v_bts[self.hov_grp][self.hov_id]["xy"][1] + self.v_bts[self.hov_grp][self.hov_id]["siz"][1]:
                if self.v_set[self.hov_grp]["phs"] == 1:
                    self.hov_d = True
        
        return self.hov_d
    
    def inp(self, inp_mos, inp_clk):
        self.inp_mos = inp_mos
        self.inp_clk = bool(inp_clk)
        
        self.v_mos["grp"] = None
        self.v_mos["id"] = None
        
        for grp in self.v_bts:
            for id in self.v_bts[grp]:
                if self.hov(grp, id, self.inp_mos) and self.inp_clk:
                    self.v_mos["grp"] = grp
                    self.v_mos["id"] = id
    
    def phs(self, phs_dlt, phs_mos):
        self.phs_dlt = float(phs_dlt)
        self.phs_mos = phs_mos

        for grp in self.v_bts:
            for id in self.v_bts[grp]:
                if self.hov(grp, id, self.phs_mos):
                    if abs(1 - self.v_bts[grp][id]["hov"]) <= self.v_inc:
                        self.v_bts[grp][id]["hov"] = 1
                    else:
                        self.v_bts[grp][id]["hov"] += (1 - self.v_bts[grp][id]["hov"]) / (self.v_lrp / self.phs_dlt)
                else:
                    if abs(self.v_bts[grp][id]["hov"]) <= self.v_inc:
                        self.v_bts[grp][id]["hov"] = 0
                    else:
                        self.v_bts[grp][id]["hov"] += -self.v_bts[grp][id]["hov"] / (self.v_lrp / self.phs_dlt)
                
                if self.v_mos["grp"] == grp and self.v_mos["id"] == id:
                    self.v_bts[grp][id]["clk"] = 1
                else:
                    if abs(self.v_bts[grp][id]["clk"]) <= self.v_inc:
                        self.v_bts[grp][id]["clk"] = 0
                    else:
                        self.v_bts[grp][id]["clk"] += -self.v_bts[grp][id]["clk"] / (self.v_lrp * 2 / self.phs_dlt)
    
    def shw(self, shw_dlt):
        self.shw_dlt = float(shw_dlt)

        if self.v_cur["grp"] != self.v_cur["grp-vis"]:
            if self.v_set[self.v_cur["grp-vis"]]["phs"] != 0:
                if abs(self.v_set[self.v_cur["grp-vis"]]["phs"]) <= self.v_inc:
                    self.v_set[self.v_cur["grp-vis"]]["phs"] = 0
                    self.v_set[self.v_cur["grp-vis"]]["shw"] = False
                    self.v_set[self.v_cur["grp"]]["shw"] = True

                    self.v_cur["grp-vis"] = self.v_cur["grp"]
                else:
                    self.v_set[self.v_cur["grp-vis"]]["phs"] += -self.v_set[self.v_cur["grp-vis"]]["phs"] / (self.v_lrp / self.shw_dlt)
        else:
            if self.v_set[self.v_cur["grp-vis"]]["phs"] != 1:
                if abs(1 - self.v_set[self.v_cur["grp-vis"]]["phs"]) <= self.v_inc:
                    self.v_set[self.v_cur["grp-vis"]]["phs"] = 1
                else:
                    self.v_set[self.v_cur["grp-vis"]]["phs"] += (1 - self.v_set[self.v_cur["grp-vis"]]["phs"]) / (self.v_lrp / self.shw_dlt)

    def drw(self):
        for grp in self.v_bts:
            for id in self.v_bts[grp]:
                if self.v_set[grp]["shw"]:
                    pg.draw.rect(self.v_srf, self.v_txt_clr, pg.Rect(self.v_bts[grp][id]["xy"][0], self.v_bts[grp][id]["xy"][1] + self.v_siz, self.v_bts[grp][id]["siz"][0], self.v_bts[grp][id]["siz"][1]))
                    pg.draw.rect(self.v_srf, bld_clr(self.v_clr, self.v_hov_clr, self.v_bts[grp][id]["hov"]), pg.Rect(self.v_bts[grp][id]["xy"][0], self.v_bts[grp][id]["xy"][1], self.v_bts[grp][id]["siz"][0], self.v_bts[grp][id]["siz"][1]))

                    self.v_lnk.drw(self.v_bts[grp][id]["num"], (self.v_bts[grp][id]["xy"][0] + self.v_siz, self.v_bts[grp][id]["xy"][1] + self.v_siz), self.v_siz, self.v_txt_clr, (0, 1), bld_clr(self.v_hov_clr, self.v_clr, self.v_bts[grp][id]["hov"]))

                    pg.draw.rect(self.v_srf, bld_clr(bld_clr(self.v_clr, self.v_hov_clr, self.v_bts[grp][id]["hov"]), self.v_txt_clr, self.v_bts[grp][id]["clk"]), pg.Rect(self.v_bts[grp][id]["xy"][0], self.v_bts[grp][id]["xy"][1], self.v_bts[grp][id]["siz"][0], self.v_bts[grp][id]["siz"][1]), 1)
                    pg.draw.rect(self.v_srf, self.v_hov_clr, pg.Rect(self.v_bts[grp][id]["xy"][0], self.v_bts[grp][id]["xy"][1], self.v_bts[grp][id]["siz"][0], self.v_bts[grp][id]["fil"] * (1 - self.v_set[grp]["phs"])))
    
    def upt(self, upt_dlt, upt_mos, upt_clk):
        self.upt_dlt = float(upt_dlt)
        self.upt_mos = upt_mos
        self.upt_clk = upt_clk

        self.inp(self.upt_mos, self.upt_clk)
        self.phs(self.upt_dlt, self.upt_mos)
        self.shw(self.upt_dlt)
        self.drw()

        if self.v_mos["grp"] != None:
            self.upt_clk = False

        return self.upt_clk