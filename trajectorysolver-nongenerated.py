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

def pos(current_state,t):
    rx,ry,rz,vx,vy,vz=current_state
    E0=[0.5+2*ry,0,-0.010-0.8*rz]
    B0=[0,5,10+50*rz]
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
