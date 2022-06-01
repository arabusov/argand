#!/usr/bin/env python3
# Support script for anim.py, intended to be reused for others
# visualizations.
# Copyright (c) 2022 Andrei Rabusov
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from bw import bw, mpi, mtau, Fa1a1p
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp
from utils import conf_mlp

BW = np.vectorize (bw)
dM3pi = 0.005
dM2pi = 0.01
m3pis = np.arange (3*mpi, mtau, dM3pi)
    #BW (m3pi**2, 1.260, 0.300, 1)*
ampl = np.array ([ Fa1a1p (m3pi**2, 1.275)*
    BW (np.arange (2*mpi, m3pi, dM2pi)**2, 0.770, 0.150, 1)
    for m3pi in m3pis])

def magnitude_1D ():
    qqs = m3pis**2
    fig, ax = plt.subplots(1, 2, figsize=(18,8))
    FF=np.vectorize (bw)
    a1widths = [0.150, 0.3, 0.4, 0.6]
    for a1width in a1widths:
        sample = FF (qqs, 1.260, a1width, 1)
        sample /= np.nanmax (np.abs (sample))
        ax[0].plot (m3pis, np.abs (sample), lw=2,
                label='$\\Gamma(\\text{a}_1)='+str(int(1000*a1width))+'$ [GeV]')
        ax[1].plot (m3pis, np.angle (sample, True), lw=2)
    ax[0].grid(True)
    ax[0].legend ()
    ax[0].set (xlabel='$m(3\pi)$ [GeV]', ylabel='$\\text{a}_1(1260)$ magnitude/max magnitude')
    ax[0].set (title='$m[\\text{a}_1(1260)]=1.26$ [GeV]')
    ax[1].set (xlabel='$m(3\pi)$ [GeV]', ylabel='$\\text{a}_1(1260)$ phase [deg]')
    ax[1].grid(True)

if __name__=="__main__":
    conf_mlp (font_size=14)
    magnitude_1D ()
    plt.tight_layout ()
    plt.show ()
    plt.close ()
