import matplotlib.pyplot as plt
import numpy as np


xVertAxis = [1000,2500,5000,7500,10000,15000,20000,25000,30000]
yVertAxis = [250810,307816,397457,510223,620405,855690,1094346,1607884,2353594]
plt.subplot(211)
plt.title('Phong Shader')
plt.xlabel('Number of Polygons')
plt.ylabel('Render time (ns)')
plt.plot(xVertAxis, yVertAxis, 'b-')
plt.plot(xVertAxis, yVertAxis, 'ro')
plt.show()


xVertAxis = [1000,2500,5000,7500,10000,15000,20000,25000,30000]
yVertAxis = [np.log(250810),np.log(307816),np.log(397457),np.log(510223),np.log(620405),np.log(855690),np.log(1094346),np.log(1607884),np.log(2353594)] 
plt.subplot(211)
plt.title('Phong Shader')
plt.xlabel('Number of Polygons')
plt.ylabel('Render time (ns)')
plt.plot(xVertAxis, yVertAxis, 'b-')
plt.plot(xVertAxis, yVertAxis, 'ro')
plt.show()
