import numpy as np
import matplotlib.pyplot as plt
Vkr=3.8
t=0
tstart=0
tstop=10
n=10
l1=5*16-6
w1=50*1e-6
Ec1=0.38*1e6
Vc1=Ec1*11
Isat=565
Isat1=Isat*w1
R0=Vc1/Isat1
V=np.linspace(tstart,tstop,n)
P0=(V**2)/R0
plt.plot(V,P0)
V=np.linspace(tstart,tstop,n)
P=((V**2)/R0)*((np.tanh(V/Vkr))/(V/Vkr))
plt.plot(V,P)
V=np.linspace(tstart,tstop,n)
P2=((V**2)/R0)*((np.tanh(V/Vc1))/(V/Vc1))
plt.plot(V,P2)
print(P)