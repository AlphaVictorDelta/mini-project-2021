import matplotlib.pyplot as plt
import numpy as np
import math


x = np.arange(0, 1000)
f = np.arange(0, 1000)
#g = np.sin(np.arange(0, 10, 0.01) * 2) * 1000
g=0*x
#plt.plot(x, f, '-')
#plt.plot(x, g, '-')
#plt.plot(g+70, x)
#plt.plot(x,g+30)
plt.plot(x,g)
plt.plot(f,x)
idx = np.argwhere(np.diff(np.sign(x - g))).flatten()
plt.plot(x[idx], g[idx], 'ro')
plt.show()
