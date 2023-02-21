import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter
from scipy.stats import linregress

with open('D:\\varmdata.txt') as f:
    lines = f.readlines()

k=0.0673811115

time=[]
ntcTempRaw=[]
bmpTemp=[]
bmpTryk=[]
bmpAlt=[]

for i in range(550, len(lines), 1):
    x = lines[i].split()
    time.append(int(x[1])-55000)
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



ntcTemp = ItoT(np.array(ntcTempRaw))
RealTime = np.array(time)/1000

RealTemp=[]


w = 50

for i in range(0, len(ntcTemp)-w,1) :
    slope=linregress(RealTime[i:i+w],ntcTemp[i:i+w])[0]
    RealTemp.append((slope)/k+(ntcTemp[i]+ntcTemp[i+w])/2)

RealTempHat=savgol_filter(RealTemp, 40,3)

plt.plot(RealTime[0:len(ntcTemp)-w], RealTemp[0:])
plt.plot(RealTime,ntcTemp)
#plt.plot(RealTime[200:len(ntcTemp)-w], RealTempHat[200:])
plt.show()