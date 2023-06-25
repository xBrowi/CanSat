import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter
from scipy.stats import linregress
import math
from scipy.spatial.transform import Rotation as R


with open("C:/Users/augus/Desktop/CanSat/CanSat/emilrun.txt") as f:
    lines = f.readlines()

k=0.57

time=np.array([])
ntcTempRaw=np.array([])
q1=np.array([])
q2=np.array([])
q3=np.array([])
qtime=np.array([])

#husk at fixe index

for i in range(0, len(lines)-0, 1):
    x = lines[i].split()
    time=np.append(time, int(x[1]))
    #ntcTempRaw=np.append(ntcTempRaw,int(x[1]))
    if x[9] != 'a':
        q1=np.append(q1,float(x[9]))
        q2=np.append(q2,float(x[10]))
        q3=np.append(q3,float(x[11]))
    else:
        q1=np.append(q1,q1[i-1])
        q2=np.append(q2,q2[i-1])
        q3=np.append(q3,q3[i-1])

def ItoT(i):
    R = 9677 / (i / (32767*4.65/6.144 - i)) # sussy 4.65 V i stedet for 5???
    A = 0.0033535
    B = 0.00030189
    C = 0.0000056906
    return (1 / (A + B * (np.log(R / 10000)) + C * pow(np.log(R / 10000), 2)))

def PtoH(P):
    A=np.float64(102.3)
    B=np.float64(273.15+15.5)
    C=np.float64(32)
    G=np.float64(9.82)
    M=np.float64(0.02897)
    R=np.float64(8.31446261815324)
    return (G*M*C-np.log(P/A)*R*B)/(G*M)


q0 = np.sqrt(1.0 - ((q1 * q1) + (q2 * q2) + (q3 * q3)))

#QUATERNION TO EULER
'''

q2sqr = q2 * q2

# roll (x-axis rotation)
t0 = +2.0 * (q0 * q1 + q2 * q3)
t1 = +1.0 - 2.0 * (q1 * q1 + q2sqr)
roll = np.arctan2(t0, t1) #* 180.0 / np.pi

# pitch (y-axis rotation)
t2 = +2.0 * (q0 * q2 - q3 * q1)
for i in range(0,len(t2)):
    if t2[i] > 1: t2[i]=1
    if t2[i] < -1: t2[i]=-1
pitch = np.arcsin(t2) #* 180.0 / np.pi

# yaw (z-axis rotation)
t3 = +2.0 * (q0 * q3 + q1 * q2)
t4 = +1.0 - 2.0 * (q2sqr + q3 * q3)
yaw = np.arctan2(t3, t4) #* 180.0 / np.pi
'''
roll=np.array([])
pitch=np.array([])
yaw=np.array([])
RotMatrix=[]


for i in range(0,len(q1)):
    r=R.from_quat([q1[i],q2[i],q3[i],q0[i]])
    roll=np.append(roll,r.as_euler('xyz')[0])
    pitch=np.append(pitch,r.as_euler('xyz')[1])
    yaw=np.append(yaw,r.as_euler('xyz')[2])
    RotMatrix.append(r.as_matrix())


plt.plot(time, roll)
plt.plot(time, pitch)
plt.plot(time, yaw, color='green')
plt.show()

r=R.from_quat([q1[0],q2[0],q3[0],q0[0]])
print(r.as_matrix())
print(RotMatrix[0])
'''
plt.plot(time,ntcTempRaw)
plt.show()


ntcTemp=ItoT(ntcTempRaw)
TimeSec=time/1000
ntcTempSavgol=savgol_filter(ntcTemp,40,1)
RegTemp=np.array([])
RegTime=np.array([])

plt.plot(TimeSec,ntcTemp-273.15)
#plt.scatter(TimeSec,ntcTempSavgol-273.15,color='red')

ntcTempSlope=np.array([])

w=4

for i in range(0, len(ntcTemp)-w,1) :
    slope=linregress(TimeSec[i:i+w],ntcTempSavgol[i:i+w])[0]
    ntcTempSlope=np.append(ntcTempSlope,slope)

Temp=(ntcTempSlope/k)+ntcTemp[int(w/2):int(-w/2)]

plt.plot(TimeSec[int(w/2):int(-w/2)],Temp-273.15) #cutter enderne af fordi regression
plt.show()

'''