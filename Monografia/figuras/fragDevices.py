# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 20}
plt.rc('font', **font)

xVertAxis = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]
gouraud = [1943258160.0, 1944383760.0, 1945631883.8709676, 1946109043.9024391, 1946808416.8421052,
           1947108571.7647059, 1947508109.2682927, 1947670112.0, 1947788202.9473684, 1947938761.1650486, 1948037266.6666667, 1948240764.0, 1948429492.330827]


gouraud_htc = [28571181.4671815, 29952830.98818662, 30824440.443149962, 31210850.342205785, 32135093.186556302,
               32813717.041561458, 33218746.08020404, 33362857.389411561, 33460576.080783326, 33570981.788074262,
               33688712.752732851, 33888605.434516966, 34032843.717745915]


plt.title(u'Asymptotic Computational Complexity')
plt.xlabel(u'Number of Polygons',fontsize=24)
plt.ylabel(u'Fragment Instructions/s',fontsize=24)
plt.plot(xVertAxis, gouraud, 'y-',label='Gouraud Shader - Nexus 4')
plt.plot(xVertAxis, gouraud_htc, 'b-',label='Gouraud Shader - HTC One')
plt.legend(loc="upper left", bbox_to_anchor=[0.0, 0.5],
           ncol=1, shadow=True, title="Legend")

plt.show()
