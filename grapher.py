import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl 
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import axes3d
from scipy.signal import square

xo=xyz[:,0]
yo= xyz[:,1]
zo=xyz[:,2]
plt.figure()
plt.plot(xo,yo,label='xy')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(xo,zo,label='xz')
plt.plot(yo,zo,label='yz')
plt.legend()

X, Y, Z =  np.meshgrid(x[10:190:10],y[10:190:10],z[10:190:10],indexing='ij')

xi,yi,zi=xyz[:,0],xyz[:,1],xyz[:,2]

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='3d')
ax.scatter3D(xi, yi, zi,s=1, color='purple') 

ax.quiver(X, Y, Z, Bx[10:190:10,10:190:10,10:190:10], By[10:190:10,10:190:10,10:190:10], Bz[10:190:10,10:190:10,10:190:10],length=0.4,alpha=0.15,color='Blue')
ax.quiver(X, Y, Z, Ex[10:190:10,10:190:10,10:190:10], Ey[10:190:10,10:190:10,10:190:10], Ez[10:190:10,10:190:10,10:190:10],length=10,alpha=0.2,color='red',label='e-field')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.view_init(elev=0,azim=-90)
