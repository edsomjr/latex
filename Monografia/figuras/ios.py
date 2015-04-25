# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 20}
plt.rc('font', **font)

xVertAxis = [10000.0,20100.0,30000.0,40678.0,50679.0,60662.0,80256.0,152840.0]
gouraud = [697507.0,1273148.0,1805226.0,2308124.0,2709994.0,3145284.0,4101440.0,5253174.0]
gouraud_iphone = [60000.0, 69000.0, 70000.0, 78000.0, 81000.0, 85000.0, 89000.0, 100000.0]
gouraud_ipad = [44000.0, 49000.0, 55000.0, 59000.0, 64000.0, 73000.0, 81000.0, 90000.0]

plt.title(u'Asymptotic Computational Complexity')
plt.xlabel(u'Number of Polygons',fontsize=24)
plt.ylabel('Time (ns)',fontsize=24)
plt.plot(xVertAxis, gouraud, 'y-',label='Gouraud Shader - Nexus 4')
plt.plot(xVertAxis, gouraud_iphone, 'r-',label='Gouraud Shader - iPhone5s')
plt.plot(xVertAxis, gouraud_ipad, 'b-',label='Gouraud Shader - iPad Air')

plt.legend(loc="upper left", bbox_to_anchor=[0.45, 0.63],
           ncol=1, shadow=True, title="Legend")

plt.show()
