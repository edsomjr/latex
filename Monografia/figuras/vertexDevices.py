# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 20}
plt.rc('font', **font)


xVertAxis = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]
gouraud = [39314514.0, 61547760.0, 106135920.0, 152053920.0, 203144400.0, 235964653.09090909, 281129040.0, 312704220.0,
           353923180.80000001, 380720880.0, 409447718.39999998, 443619024.0, 469564080.0]

gouraud_htc = [40330378.378378399, 63784342.412451394, 109941291.828794, 153750229.00763401, 213304857.22880456,
               249646483.62627533, 303378604.65116304, 337383658.52529198, 368156228.13688201, 408307605.54680502,
               447746255.63909799, 463264000.0, 531982590.64931899]


plt.title(u'Asymptotic Computational Complexity')
plt.xlabel(u'Number of Polygons',fontsize =24)
plt.ylabel(u'Vertex Instructions/s',fontsize=24)
plt.plot(xVertAxis, gouraud, 'y-',label='Gouraud Shader - Nexus 4')
plt.plot(xVertAxis, gouraud_htc, 'b-',label='Gouraud Shader - HTC One')
plt.legend(loc="upper left", bbox_to_anchor=[0.0, 1.0],
           ncol=1, shadow=True, title="Legend")

plt.show()
