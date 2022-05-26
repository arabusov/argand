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

BW = np.vectorize (bw)
dM3pi = 0.005
dM2pi = 0.01
m3pis = np.arange (3*mpi, mtau, dM3pi)
    #BW (m3pi**2, 1.260, 0.300, 1)*
ampl = np.array ([ Fa1a1p (m3pi**2)*
    BW (np.arange (2*mpi, m3pi, dM2pi)**2, 0.770, 0.150, 1)
    for m3pi in m3pis])