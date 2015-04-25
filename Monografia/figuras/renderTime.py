# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 20}
plt.rc('font', **font)

xVertAxis = [10000.0,20100.0,30000.0,40678.0,50679.0,60662.0,80256.0,152840.0]
gouraud = [697507.0,1273148.0,1805226.0,2308124.0,2709994.0,3145284.0,4101440.0,5253174.0]
phong =  [768793.0, 1375062.0, 1917230.0, 2446076.0, 2881826.0, 3326094.0, 4354622.0, 5492126.0]
red =  [622876.0, 1084351.0, 1503667.0, 1968586.0, 2364504.0, 2741598.0, 3660865.0, 4438432.0]
toon = [625896.0, 1128030.0, 1598755.0, 2056096.0, 2460048.0, 2856074.0, 3787202.0, 4379543.0]
flat =  [650290.0, 1134116.0, 1594429.0, 2054351.0, 2440068.0, 2850502.0, 3803729.0, 4396133.0]
random = [628438.0, 1123070.0, 1601188.0, 2072194.0, 2462815.0, 2849012.0, 3791349.0, 4552120.0]
texture = [626566.0, 1127398.0, 1604174.0, 2069526.0, 2478315.0, 2877501.0, 3786759.0, 4605933.0]
cubemap =  [745818.0, 1225848.0, 1702577.0, 2273715.0, 2623740.0, 3059771.0, 3929830.0, 5006836.0]
reflection = [856287.0, 1514258.0, 1965644.0, 2505458.0, 2942499.0, 3344280.0, 4205371.0, 5716238.0]

plt.title(u'Asymptotic Computational Complexity')
plt.xlabel(u'Number of Polygons',fontsize=24)
plt.ylabel('Time (ns)',fontsize=24)
plt.plot(xVertAxis, gouraud, 'y-',label='Gouraud Shader')
plt.plot(xVertAxis, phong, 'b-',label='Phong Shader')
plt.plot(xVertAxis, red, 'r-',label='Red Shader')
plt.plot(xVertAxis, flat, '#ff99ff',label='Flat Shader')
plt.plot(xVertAxis, toon, 'g-',label='Toon Shader')
plt.plot(xVertAxis, random, 'm-',label='Random Shader')
plt.plot(xVertAxis, texture, 'c-',label='Texture Shader')
plt.plot(xVertAxis, cubemap, 'k-',label='Cubemap Shader')
plt.plot(xVertAxis, reflection, '0.75',label='Reflection Shader')
plt.legend(loc="upper left", bbox_to_anchor=[0.05, 0.93],
           ncol=1, shadow=True, title="Legend")

plt.show()
