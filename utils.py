#!/usr/bin/env python3

import matplotlib as mp
from tex_preamble import TeX_preamble

def conf_mlp (font_size=14, font_family="serif"):
    mp.rc("font",  **dict(size=font_size,
        family=font_family,serif=["Computer Modern"]))
    mp.rc("lines", **dict(linewidth=0.5))
    mp.rc("text", usetex=True)
    mp.rc("text.latex",preamble=TeX_preamble)
