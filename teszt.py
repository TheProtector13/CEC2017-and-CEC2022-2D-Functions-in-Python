import numpy as np
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from Functions import Functions

F = Functions()

x = np.linspace(-100, 100, 1000)
y = np.linspace(-100, 100, 1000)
X, Y = np.meshgrid(x, y)
Z = np.empty_like(X)

for i in range(len(X[0])):
    for j in range(len(X[0])):
        Z[i,j] = F.C22_2(X[i,j],Y[i,j])
        #Z[i,j] = F.Test(X[i,j],Y[i,j])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(X, Y, Z, cmap='plasma')
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.xaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))
ax.yaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))
ax.zaxis.pane.set_facecolor((1.0, 1.0, 1.0, 0.0))

ax.set_facecolor((1.0, 1.0, 1.0, 0.0))

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.grid(True)
# contour

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
cf = ax2.contourf(X, Y, Z, levels=200, cmap='viridis')
cs = ax2.contour(X, Y, Z, levels=15, cmap='autumn', linewidths=0.5)
fig2.colorbar(cf)
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
ax2.set_aspect('equal')
fig2.show()

print(np.max(Z))

plt.show()
