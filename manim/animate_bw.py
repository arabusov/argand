#!/usr/bin/env python3
# Requirements: manim
# If install in $HOME/.local add $HOME/.local/bin into PATH
# How to run:
#
#   manimgl animate_bw.py

import numpy as np

from manimlib import *

mpi = 0.13957
mtau = 1.77686

fmt='{:.3f}'
M = 0.770
G = 0.150
l = 1
pole_text = '('+fmt.format (M) + ' - i' + fmt.format (G)+') [GeV]'

scale = 2

M *= scale
G *= scale

def bw (s, m, g, l):
    mp = 4*mpi**2;
    msq = m**2;
    w = np.sqrt (s);
    wgs = 0.0;
    qs = np.sqrt (np.abs ((s-mp)*s))/w;
    qm = np.sqrt (np.abs ((msq-mp)*msq))/m;
    ipow = 2*l+1;
    wgs = g*(msq/w)*(qs/qm)**ipow;
    denom = (msq-s)**2+wgs**2
    return 0.75*complex (msq*(msq-s)/denom, msq*wgs/denom)

class BreitWigner (Scene ):
    def construct(self):

        # Complex map
        c_grid = ComplexPlane((-2*scale,2*scale),(-1*scale, 1*scale))
        moving_c_grid = c_grid.copy()
        moving_c_grid.prepare_for_nonlinear_transform()
        c_grid.set_stroke(BLUE_E, 1)
        c_grid.add_coordinate_labels(font_size=24)
        complex_map_words = TexText("""
            $s \\rightarrow $ Breit-Wigner $(s)$
        """)
        complex_map_words.to_corner(UR)
        complex_map_words.set_stroke(BLACK, 5, background=True)
        pole=Dot (c_grid.n2p (complex (M, -G)), color=YELLOW, radius=0.1)
        pole_title=Text(pole_text).next_to(pole, DOWN)

        self.add (pole)
        self.play(
            Write(c_grid, run_time=3),
            FadeIn(moving_c_grid),
            Write(complex_map_words),
        )
        self.wait()
        BW = np.vectorize (bw)
        self.play(
            moving_c_grid.animate.apply_complex_function(lambda z: 
                BW (z, M, G, l)),
            run_time=12,
        )
        self.wait(2)
