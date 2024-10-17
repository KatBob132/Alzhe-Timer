from pynput.keyboard import Listener as lst
from pyautogui import click as clk
from time import sleep as sp
from sys import exit as ext
import pyautogui as pag

pag.FAILSAFE = False

clk_ing = False
prs = set()

def on_prs(key):
    try:
        prs.add(key.char)
    except AttributeError:
        pass

def on_rls(key):
    try:
        prs.remove(key.char)
    except AttributeError:
        pass

lsn = lst(on_press=on_prs, on_release=on_rls)
lsn.start()

while True:
    if "n" in prs:
        clk_ing = True
    if "m" in prs:
        clk_ing = False
    if "v" in prs:
        ext()
    
    if clk_ing:
        clk()

    sp(0.01)