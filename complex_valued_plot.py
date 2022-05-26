#!/usr/bin/env python3
# Taken from  https://stackoverflow.com/questions/56577154/matplotlib-heatmap-of-complex-numbes-modulus-and-phase-as-hue-and-value

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mp

from a1rho import m3pis, mtau, mpi, dM2pi, ampl

from tex_preamble import TeX_preamble
def conf_mlp (font_size=14, font_family="serif"):
    mp.rc("font",  **dict(size=font_size,
        family=font_family,serif=["Computer Modern"]))
    mp.rc("lines", **dict(linewidth=0.5))
    mp.rc("text", usetex=True)
    mp.rc("text.latex",preamble=TeX_preamble)

def complex_valued_plot(cmplxarray):
    # Creating the black cover layer

    black = np.full((*cmplxarray.shape, 4), 0.)
    black[:,:,-1] = np.abs(cmplxarray) / np.nanmax (np.abs(cmplxarray))
    black[:,:,-1] = 1 - black[:,:,-1]
    phis = np.angle (cmplxarray, deg=True)
    # Actual plot

    fig, ax = plt.subplots(figsize=(9,8))
    pc1 = ax.imshow(phis, cmap='hsv', extent=[3*mpi,mtau, 2*mpi, mtau])
    # Plotting the modulus array as the 'value' part
    ax.imshow(black, extent=[3*mpi,mtau, 2*mpi, mtau])
    ax.set (xlabel='$m(3\pi)$ [GeV]', ylabel='$m(2\pi)$ [GeV]')
    cbar1 = fig.colorbar (pc1, ax=ax)
    cbar1.ax.set_ylabel ('Phase [deg]', rotation=270)

m2pis = np.arange (2*mpi, mtau, dM2pi)
field = np.zeros ((m2pis.size, m3pis.size), dtype=complex)
field.fill (np.nan)
for i, isobar in enumerate (ampl):
    size = np.shape (isobar) [0]
    field [len (m2pis)-size:,i] = np.flip (isobar)

conf_mlp (font_size=14)
complex_valued_plot (field)
plt.tight_layout ()

import argparse
parser = argparse.ArgumentParser ()
parser.add_argument ("--output", help="Output file to save figure")
args = parser.parse_args ()

if args.output is not None:
    plt.savefig (args.output)
    plt.close ()
else:
    plt.show ()
    plt.close ()

