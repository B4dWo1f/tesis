#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
 Evolution of the GB bands as a funcion of the SK parameters
"""

import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()
for Hs in [-1,0,1]: #np.linspace(-5,5,51):
   X,Y = [],[]
   for Vsss in [-2.5]:
      for Vsps in np.linspace(-15,15,31):
         H = np.matrix([[  Hs, Vsss, Vsps],
                        [Vsss, -8.8,    0],
                        [Vsps,    0,    0]])
         e,v = np.linalg.eig(H)
         for ie in e:
            X.append(Vsps)
            Y.append(ie)
   ax.scatter(X,Y,label='Hs=%s'%(Hs))
plt.show()
