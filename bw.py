#!/usr/bin/env python3
# This script is C&P from TAUOLA f3pi.f
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
mpi = 0.13957
mtau = 1.77686

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
    return complex (msq*(msq-s)/denom, msq*wgs/denom)

def wga1n (s):
    q0 = 6.28450
    q1 = -2.95950
    q2 = 4.33550
    p0 = -15.411
    p1 = 32.08800
    p2 = -17.6660
    p3 = 4.9355
    p4 =  -0.37498;
    sth = 0.1676
    if s < sth:
        return 0.;
    if s < 0.823:
        return q0*(s-sth)**3*(1.+q1*(s-sth)
            + q2*(s-sth)**2)
    else:
        return p0 + p1*s + p2*s**2 + p3* s**3 + p4* s**4;

def wga1c (s):
    q0 = 5.809
    q1 = -3.0098
    q2 = 4.5792
    p0 = -13.914
    p1 = 27.679
    p2 = -13.393
    p3 = 3.1924
    p4 =  -0.10487;
    sth = 0.1753;
    if s < sth:
        return 0.
    if s < 0.823:
        return q0*(s-sth)**3 *(1.+q1*(s-sth)
            + q2*(s-sth)**2);
    else:
        return p0 + p1*s + p2*s**2 + p3* s**3 + p4* s**4;

def wga1 (qq):
    gkst = 0.;
    mkst = 0.894;
    mk = 0.496;
    c3pi = 0.2384**2;
    ckst = 4.7621**2 * c3pi;
    mk1sq = (mkst+mk)**2;
    mk2sq = (mkst-mk)**2;
    if qq > mk1sq:
        gkst = np.sqrt ((qq-mk1sq)*(qq-mk2sq))/(2.*qq);
    return c3pi*(wga1c (qq) + wga1n (qq)) + ckst*gkst;

def Fa1a1p (qq):
    c3pi = 0.2384**2;
    ma1 = 1.275;
    ma1sq = ma1**2
    ga1 = 0.700;
    ma1p = 1.461;
    ma1psq = ma1p**2
    ga1p = 0.250;
    beta_a1 = complex (0., 0);
    ckst = 4.7621**2 * c3pi;
    gg1 = ma1*ga1/(1.3281*0.806);
    gg2 = ma1p*ga1p/(1.3281*0.806);

    gf = wga1 (qq);
    fg1 = gg1*gf;
    fg2 = gg2*gf;
    f1 = complex (-ma1sq, 0.)/complex(qq-ma1sq, fg1);
    f2 = complex (-ma1psq, 0.)/complex(qq-ma1psq, fg2);
    return f1+beta_a1*f2;

