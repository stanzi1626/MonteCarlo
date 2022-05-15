import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111, projection='3d')

xdata = np.zeros(0)
ydata = np.zeros(0)
zdata = np.zeros(0)

for j in range(0, 1000):
    x = np.random.uniform(-1, 1, 1)
    y_limit = np.sqrt(1 - x**2)
    y = np.random.uniform(-y_limit, y_limit, 1)
    i = np.random.uniform(0, 1, 1)
    if  i < 0.5:
        z = np.sqrt(1-x**2-y**2)
    else:
        z = -np.sqrt(1-x**2-y**2)
    xdata = np.append(xdata, x)
    ydata = np.append(ydata, y)
    zdata = np.append(zdata, z)

ax.scatter(xdata, ydata, zdata)
plt.show()