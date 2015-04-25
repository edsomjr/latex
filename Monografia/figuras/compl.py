# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


xVertAxis = [1.0,1.5,2.0,2.5,3.0,3.5,4.0]
constant = [10,10,10,10,10,10,10]
n = xVertAxis
quad = [np.power(xVertAxis[0],2),np.power(xVertAxis[1],2),np.power(xVertAxis[2],2),np.power(xVertAxis[3],2),np.power(xVertAxis[4],2),np.power(xVertAxis[5],2),
        np.power(xVertAxis[6],2)]
cubic = [np.power(xVertAxis[0],3),np.power(xVertAxis[1],3),np.power(xVertAxis[2],3),np.power(xVertAxis[3],3),np.power(xVertAxis[4],3),np.power(xVertAxis[5],3),
         np.power(xVertAxis[6],3)]
log = [np.log(xVertAxis[0]),np.log(xVertAxis[1]),np.log(xVertAxis[2]),np.log(xVertAxis[3]),np.log(xVertAxis[4]),np.log(xVertAxis[5]),np.log(xVertAxis[6])]
nlog = [xVertAxis[0] * np.log(xVertAxis[0]),xVertAxis[1] * np.log(xVertAxis[1]),xVertAxis[2] * np.log(xVertAxis[2]),xVertAxis[3] * np.log(xVertAxis[3]),
        xVertAxis[4] * np.log(xVertAxis[4]),xVertAxis[5] * np.log(xVertAxis[5]), xVertAxis[6] * np.log(xVertAxis[6])]
exp = [np.exp(xVertAxis[0]),np.exp(xVertAxis[1]),np.exp(xVertAxis[2]),np.exp(xVertAxis[3]),np.exp(xVertAxis[4]),np.exp(xVertAxis[5]),np.exp(xVertAxis[6])]

plt.title(u'Complexidade Assintótica')
plt.xlabel(u'Número de entradas')
plt.ylabel('Tamanho resultante')
plt.plot(xVertAxis, constant, 'y-',label='Constante')
plt.plot(xVertAxis, n, 'b-', label = "Linear")
plt.plot(xVertAxis, quad, 'r-', label = u"Quadrática")
plt.plot(xVertAxis, cubic, 'g-', label = u"Cúbica")
plt.plot(xVertAxis, log, 'm-', label = "Log N")
plt.plot(xVertAxis, nlog, 'c-', label = "N Log N")
plt.plot(xVertAxis, nlog, 'k-', label = "Exponencial")
plt.legend(loc="upper left", bbox_to_anchor=[0.0, 1.0],
           ncol=1, shadow=True, title="Legenda")

plt.show()
