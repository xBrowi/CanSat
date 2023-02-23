import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter
from scipy.stats import linregress

with open('D:\\varmeluft2.txt') as f:
    lines = f.readlines()

k=0.16
k1=1/2000
k4=0.000000002

time=[]
ntcTempRaw=[]
bmpTemp=[]
bmpTryk=[]
bmpAlt=[]

for i in range(000, len(lines), 1):
    x = lines[i].split()
    time.append(int(x[1])-00000)
    ntcTempRaw.append(int(x[2]))
    """bmpTemp.append(float(x[3]))
    bmpTryk.append(float(x[4]))
    bmpAlt.append(float(x[5]))"""

def ItoT(i):
    R = 10000 / (i / (1024 - i))
    A = 0.003354016
    B = 0.000256985
    C = 0.000002620131
    D = 0.00000006383091
    return (1 / (A + B * (np.log(R / 10000)) + C * pow(np.log(R / 10000), 2) + D * pow(np.log(R / 10000), 3)) - 273.15)


w = 10

ntcTemp = ItoT(np.array(ntcTempRaw))
RealTime = np.array(time)/1000
RealTimeTemp = RealTime+w/10
RealTemp=[]


for i in range(0, len(ntcTemp)-w,1) :
    slope=linregress(RealTime[i:i+w],ntcTemp[i:i+w])[0]
    RealTemp.append((slope)/(k+k1*((ntcTemp[i]+ntcTemp[i+w])/2)+k4*(((ntcTemp[i]+ntcTemp[i+w])/2)**4))+(ntcTemp[i]+ntcTemp[i+w])/2)
    if (ntcTemp[i]>49 and ntcTemp[i]<51):
        print(slope)

RealTempHat=savgol_filter(RealTemp, 40,3)

plt.plot(RealTimeTemp[0:len(ntcTemp)-w], RealTemp[0:], label='Omgivelser')
plt.plot(RealTime,ntcTemp, label='Sensor')
plt.legend()
plt.xlabel('Tid [s]')
plt.ylabel('Temperatur [$^\circ$C]')
plt.grid()
#plt.plot(RealTime[200:len(ntcTemp)-w], RealTempHat[200:])
plt.show()