import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl 
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import axes3d
from scipy.signal import square

h=0.05
x = np.arange(0,10,h)
y = np.arange(0,10,h)
z= np.arange(0,10,h)

q=1.6e-19
m=9.31e-20

def indexfindx(r):
    h=0.05
    x = np.arange(0,10,h)
    for i in x:
        if r>i:
            continue
        if r==i:
            break
        if r<i:
            break
    return np.where(x==i)[0][0]

def indexfindy(r):
    h=0.05
    y = np.arange(0,10,h)
    for i in y:
        if r>i:
            continue
        if r==i:
            break
        if r<i:
            break
    return np.where(y==i)[0][0]

def indexfindz(r):
    h=0.05
    z = np.arange(0,10,h)
    for i in z:
        if r>i:
            continue
        if r==i:
            break
        if r<i:
            break
    return np.where(z==i)[0][0]

Bx=np.load('C:/Users/User/Desktop/plasmas/Bx.npy')
By=np.load('C:/Users/User/Desktop/plasmas/By.npy')
Bz=np.load('C:/Users/User/Desktop/plasmas/Bz.npy')
Ex=np.ones((len(x),len(y),len(z)))*0
Ey=np.ones((len(x),len(y),len(z)))*0.01
Ez=np.ones((len(x),len(y),len(z)))*0.01


def Etime(t,t0):
    return square(2*np.pi*(1/(2*t0))*t)

def pos11(current_state,t):
    rx,ry,rz,vx,vy,vz=current_state
    # Bx=np.load('C:/Users/User/Desktop/plasmas/Bx.npy')
    # By=np.load('C:/Users/User/Desktop/plasmas/By.npy')
    # Bz=np.load('C:/Users/User/Desktop/plasmas/Bz.npy')
    E0=[0,Etime(t,25)*0.01,-Etime(t,25)*0.01]
    B0=[Bx[indexfindx(rx),indexfindy(ry),indexfindz(rz)],By[indexfindx(rx),indexfindy(ry),indexfindz(rz)],Bz[indexfindx(rx),indexfindy(ry),indexfindz(rz)]]
    B=(q*B0[2])/m
    C=(q*B0[1])/m
    D=(q*E0[1])/m 
    E=(q*B0[0])/m
    F=(q*B0[2])/m 
    G=(q*E0[2])/m 
    H=(q*B0[1])/m 
    I=(q*B0[0])/m 
    
    
    d2rxdt2=q*E0[0]/m+B*vy-C*vz
    d2rydt2=D+E*vz-F*vx
    d2rzdt2=G+H*vx-I*vy
    
    return [vx,vy,vz,d2rxdt2,d2rydt2,d2rzdt2]


y0=[5.700,6,2.5,0.1,-0.1,-0.1]
t=np.arange(0,400,0.1)
xyz=odeint(pos11,y0,t)
