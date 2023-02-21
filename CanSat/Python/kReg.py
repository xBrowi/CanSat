import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

with open('D:\\varmdata.txt') as f:
    lines = f.readlines()

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




def func(x, a, b, c):
    return a * np.exp(-b * x) + c

x = np.array(time)/1000

plt.plot(x, ntcTemp)
plt.show()

popt, pcov = curve_fit(func, x, ntcTemp, p0=[92, 0.067, 25])

plt.figure()
plt.plot(x, ntcTemp, 'ko', label="Original Noised Data")
plt.plot(x, func(x, *popt), 'r-', label="Fitted Curve")
plt.legend()
plt.show()

print(popt)
print(pcov)

