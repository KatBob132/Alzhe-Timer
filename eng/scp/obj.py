from scp.utl import *
from scp.fnc import *

class btt_obj:
    def __init__(self, chc_clr, bck_clr, for_clr, hov_fus, grp_fus, srf, txt_lnk, txt_siz, cur_grp):
        self.chc_clr = cfg_clr(chc_clr)
        self.bck_clr = cfg_clr(bck_clr)
        self.for_clr = cfg_clr(for_clr)

        self.hov_fus = float(hov_fus)
        self.grp_fus = float(grp_fus)

        self.srf = srf

        self.txt_lnk = txt_lnk
        self.txt_siz = int(txt_siz)

        self.cur_grp = str(cur_grp)
        self.wnt_grp = str(cur_grp)

        self.inc = 0.01
        self.dct = {}
        
        self.grp_dat = {}

    def add_grp(self, add_grp_tag):
        self.add_grp_tag = str(add_grp_tag)

        self.dct[self.add_grp_tag] = {}
        
        if self.cur_grp == self.add_grp_tag:
            self.grp_dat[self.add_grp_tag] = {"shw": 0}
        else:
            self.grp_dat[self.add_grp_tag] = {"shw": 1}
    
    def add_btt(self, add_btt_grp, add_btt_txt, add_btt_xy, add_btt_cnr=(False, False)):
        self.add_btt_grp = str(add_btt_grp)
        self.add_btt_tag = int(len(self.dct[self.add_btt_grp]))

        self.add_btt_txt = str(add_btt_txt)
        self.add_btt_xy = [int(add_btt_xy[0]), int(add_btt_xy[1])]
        self.add_btt_siz = self.txt_lnk.siz(self.add_btt_txt, self.txt_siz, (0, 1))
        self.add_btt_cnr = (bool(add_btt_cnr[0]), bool(add_btt_cnr[1]))

        for a in range(2):
            self.add_btt_siz[a] += self.txt_siz * 2

            if self.add_btt_cnr[a]:
                self.add_btt_xy[a] += -int(self.add_btt_siz[a] / 2)

        self.dct[self.add_btt_grp][self.add_btt_tag] = {}

        self.dct[self.add_btt_grp][self.add_btt_tag]["txt"] = self.add_btt_txt
        self.dct[self.add_btt_grp][self.add_btt_tag]["xy"] = self.add_btt_xy
        self.dct[self.add_btt_grp][self.add_btt_tag]["siz"] = self.add_btt_siz
        self.dct[self.add_btt_grp][self.add_btt_tag]["clr"] = [self.for_clr[0], self.for_clr[1], self.for_clr[2]]
        self.dct[self.add_btt_grp][self.add_btt_tag]["cnr"] = self.add_btt_cnr

        self.dct[self.add_btt_grp][self.add_btt_tag]["shw"] = [0, self.dct[self.add_btt_grp][self.add_btt_tag]["siz"][1] + self.txt_siz]
        self.dct[self.add_btt_grp][self.add_btt_tag]["shw"][0] = self.dct[self.add_btt_grp][self.add_btt_tag]["shw"][1] * self.grp_dat[self.add_btt_grp]["shw"]
    
    def chg_grp(self, chg_grp_tag):
        self.chg_grp_tag = str(chg_grp_tag)
        self.wnt_grp = self.chg_grp_tag

    def hov(self, hov_grp, hov_tag, hov_xy):
        self.hov_grp = str(hov_grp)
        self.hov_tag = int(hov_tag)

        self.hov_xy = (int(hov_xy[0]), int(hov_xy[1]))
        self.hov_d = False

        self.hov_dat = (self.dct[self.hov_grp][self.hov_tag]["xy"], self.dct[self.hov_grp][self.hov_tag]["siz"])

        if self.hov_xy[0] >= self.hov_dat[0][0] and self.hov_xy[0] <= self.hov_dat[0][0] + self.hov_dat[1][0]:
            if self.hov_xy[1] >= self.hov_dat[0][1] and self.hov_xy[1] <= self.hov_dat[0][1] + self.hov_dat[1][1]:
                self.hov_d = True
        
        return self.hov_d
    
    def clr(self, clr_dlt, clr_xy):
        self.clr_dlt = float(clr_dlt)
        self.clr_xy = (int(clr_xy[0]), int(clr_xy[1]))

        for grp in self.dct:
            for btt in self.dct[grp]:
                self.clr_hov = self.hov(grp, btt, self.clr_xy)

                for a in range(3):
                    if self.clr_hov:
                        self.dct[grp][btt]["clr"][a] += (self.bck_clr[a] - self.dct[grp][btt]["clr"][a]) / (self.hov_fus / self.clr_dlt)

                        if abs(self.bck_clr[a] - self.dct[grp][btt]["clr"][a]) < self.inc:
                            self.dct[grp][btt]["clr"][a] = self.bck_clr[a]
                    else:
                        self.dct[grp][btt]["clr"][a] += (self.for_clr[a] - self.dct[grp][btt]["clr"][a]) / (self.hov_fus / self.clr_dlt)

                        if abs(self.for_clr[a] - self.dct[grp][btt]["clr"][a]) < self.inc:
                            self.dct[grp][btt]["clr"][a] = self.for_clr[a]
    
    def grp(self, grp_dlt):
        self.grp_dlt = float(grp_dlt)

        if self.cur_grp != self.wnt_grp:
            self.grp_dat[self.cur_grp]["shw"] += (1 - self.grp_dat[self.cur_grp]["shw"]) / (self.grp_fus / self.grp_dlt)

            if abs(1 - self.grp_dat[self.cur_grp]["shw"]) < self.inc:
                self.grp_dat[self.cur_grp]["shw"] = 1
                self.cur_grp = self.wnt_grp
        else:
            if self.grp_dat[self.cur_grp]["shw"] != 0:
                self.grp_dat[self.cur_grp]["shw"] -= self.grp_dat[self.cur_grp]["shw"] / (self.grp_fus / self.grp_dlt)

                if abs(self.grp_dat[self.cur_grp]["shw"]) < self.inc:
                    self.grp_dat[self.cur_grp]["shw"] = 0

    def drw(self):
        for grp in self.dct:
            if grp == self.cur_grp:
                for btt in self.dct[grp]:
                    pg.draw.rect(self.srf, self.chc_clr, pg.Rect(self.dct[grp][btt]["xy"][0], self.dct[grp][btt]["xy"][1] + self.txt_siz, self.dct[grp][btt]["siz"][0], self.dct[grp][btt]["siz"][1]))
                    pg.draw.rect(self.srf, self.dct[grp][btt]["clr"], pg.Rect(self.dct[grp][btt]["xy"][0], self.dct[grp][btt]["xy"][1], self.dct[grp][btt]["siz"][0], self.dct[grp][btt]["siz"][1]))

                    pg.draw.rect(self.srf, self.bck_clr, pg.Rect(self.dct[grp][btt]["xy"][0], self.dct[grp][btt]["xy"][1], 1, 1))
                    pg.draw.rect(self.srf, self.bck_clr, pg.Rect(self.dct[grp][btt]["xy"][0] + self.dct[grp][btt]["siz"][0] - 1, self.dct[grp][btt]["xy"][1], 1, 1))

                    pg.draw.rect(self.srf, self.bck_clr, pg.Rect(self.dct[grp][btt]["xy"][0], self.dct[grp][btt]["xy"][1] + self.txt_siz + self.dct[grp][btt]["siz"][1] - 1, 1, 1))
                    pg.draw.rect(self.srf, self.bck_clr, pg.Rect(self.dct[grp][btt]["xy"][0] + self.dct[grp][btt]["siz"][0] - 1, self.dct[grp][btt]["xy"][1] + self.txt_siz + self.dct[grp][btt]["siz"][1] - 1, 1, 1))

                    self.txt_lnk.drw(self.dct[grp][btt]["txt"], (self.dct[grp][btt]["xy"][0] + self.txt_siz, self.dct[grp][btt]["xy"][1] + self.txt_siz), self.txt_siz, self.chc_clr, (0, 1), self.bck_clr)
                    
                    self.dct[grp][btt]["shw"][0] = self.dct[grp][btt]["shw"][1] * self.grp_dat[grp]["shw"]

                    pg.draw.rect(self.srf, self.bck_clr, pg.Rect(self.dct[grp][btt]["xy"][0], self.dct[grp][btt]["xy"][1], self.dct[grp][btt]["siz"][0], self.dct[grp][btt]["shw"][0]))
    
    
    def upt(self, upt_dlt, upt_xy):
        self.upt_dlt = float(upt_dlt)
        self.upt_xy = (int(upt_xy[0]), int(upt_xy[1]))

        self.clr(self.upt_dlt, self.upt_xy)
        self.grp(self.upt_dlt)
        self.drw()