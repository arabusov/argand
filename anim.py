#!/usr/bin/env python3
# This script is C&P from the matplotlib example ``double_pendulum'' and
# modified in a way to show argand plot evolution in m3pi.
#
# Requirements
# ============
#
#  - python3
#  - matplotlib
#  - numpy
# On most of the modern Linux distros (including Slackware) python3 is
# a part of base system. To install python libraries either use your package
# manager, or use ``pip3'' command (namely, `pip3 install matplotlib` and so
# on). MacOS users should also have python3 (and pip3) installed.
# 
# Execution
# =========
# Type `python3 sliding_pendulum.py` in your GUI Terminal. A new window with
# animation should appear on your screen automatically, if everything is
# fine.
#
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

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import argparse

from a1rho import ampl, dM3pi, m3pis

# Unpack results
x1 = np.array ([np.real (vec) for vec in ampl])
y1 = np.array ([np.imag (vec) for vec in ampl])
xmax = 13
ymax = 13

fig = plt.figure(figsize=(10, 10))
# Here you can adjust the size of the window and the limits.
ax = fig.add_subplot(autoscale_on=False, xlim=(-xmax, xmax), ylim=(-ymax,ymax))
# Pay attention, that the aspect ratio is 1
ax.set_aspect('equal')
ax.grid()

line1, = ax.plot([], [], 'o-', lw=2)
ax.set(xlabel='Re', ylabel='Im')
time_template = 'm3pi= %.1fGeV'
time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

def animate(i):
    thisx1 = x1[i]
    thisy1 = y1[i]
    line1.set_data(thisx1, thisy1)

    time_text.set_text(time_template % (m3pis[i]))
    return line1, line1, time_text


ani = animation.FuncAnimation(
    fig, animate, len(y1), interval=dM3pi*1000, blit=True)
parser = argparse.ArgumentParser ()
parser.add_argument ("--output", help="Output file to save animation")
args = parser.parse_args ()

if args.output is not None:
    ani.save(args.output, dpi=90, fps=30)
else:
    plt.show()
