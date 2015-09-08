#!/usr/bin/env python

"""
Generates golden angle plots - leaves in nature

Inspired by:
Doodling in Math Class: Spirals, Fibonacci, and Being a Plant [2 of 3]
https://www.youtube.com/watch?v=lOIP_Z_-0Hs
"""

from __future__ import division

import numpy as np
import scipy as sp
from scipy import constants
import matplotlib.pyplot as plt

golden_angle = (1/sp.constants.golden**2) * np.pi * 2

ax = plt.subplot(111, polar=True)

num_leaves = 10

for i in range(1, num_leaves+1):
    r = [0, 0.1*i]
    theta = [golden_angle * i]*2
    leaf_color = str(1 - i/num_leaves)
    ax.plot(theta, r, ls='-', color=leaf_color, lw=0.4*i)

ax.grid(True)

plt.savefig('../images/leaves.pdf')
