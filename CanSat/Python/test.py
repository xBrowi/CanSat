
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter
from scipy.stats import linregress

with open("C:/Users/augus/Downloads/test2.txt") as f:
    lines = f.readlines()[950:1250]


def ItoT(i):
    R = 10000 / (i / (1024 - i))
    A = 0.003354016
    B = 0.000256985
    C = 0.000002620131
    D = 0.00000006383091
    return (1 / (A + B * (np.log(R / 10000)) + C * pow(np.log(R / 10000), 2) + D * pow(np.log(R / 10000), 3)))

diode=[]
A1=[]
A2=[]
A3=[]
nr=[i for i in range(1, len(lines)+1)]




for i in range(0, len(lines), 1):
    x = lines[i].split()
    A1.append(int(x[0]))
    A2.append(int(x[1]))
    A3.append(float(x[2]))
    diode.append(float(x[3]))

diodeTemp=np.array(diode)-25
A1Temp=ItoT(1023-np.array(A1))-273.15-25
A2Temp=ItoT(1023-np.array(A2))-273.15-25
A3Temp=ItoT(1023-np.array(A3))-273.15-25

plt.plot(nr,diodeTemp, label="Diode")
plt.plot(nr,A1Temp, label="A1 (ntc)")
plt.plot(nr,A2Temp, label="A2 (ntc)")
plt.plot(nr,A3Temp, label="A3 (ntc)")
plt.ylabel('Temp [$^\circ$C]')
plt.xlabel('Måling nr (100ms/måling)')
plt.legend()
plt.show()

w = 10

diodeSlope=[]
RegDiode=[]

A1Slope=[]
RegA1=[]

A2Slope=[]
RegA2=[]

A3Slope=[]
RegA3=[]

for i in range(0, len(nr)-w,1) :
    slope=linregress(nr[i:i+w],diodeTemp[i:i+w])[0]
    diodeSlope.append(slope)
    RegDiode.append(diodeTemp[i+round(w/2)])

for i in range(0, len(nr)-w,1) :
    slope=linregress(nr[i:i+w],A1Temp[i:i+w])[0]
    A1Slope.append(slope)
    RegA1.append(A1Temp[i+round(w/2)])

for i in range(0, len(nr)-w,1) :
    slope=linregress(nr[i:i+w],A2Temp[i:i+w])[0]
    A2Slope.append(slope)
    RegA2.append(A2Temp[i+round(w/2)])

for i in range(0, len(nr)-w,1) :
    slope=linregress(nr[i:i+w],A3Temp[i:i+w])[0]
    A3Slope.append(slope)
    RegA3.append(A3Temp[i+round(w/2)])

plt.scatter(RegDiode,diodeSlope, label="Diode")
plt.scatter(RegA1,A1Slope, label="A1 (ntc)")
plt.scatter(RegA2,A2Slope, label="A2 (ntc)")
plt.scatter(RegA3,A3Slope, label="A3 (ntc)")
plt.legend()
plt.ylabel('dT/dt [K/s]')
plt.xlabel('Temp [$^\circ$C]')
plt.show()