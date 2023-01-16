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

plt.plot(time, ntcTempRaw)
plt.show()


def func(x, a, b, c):
    return a * np.exp(-b * x) + c

x = np.array(time)
#y = func(x, 510, 0.00005, 490)
y=np.array(ntcTempRaw)
yn = y

popt, pcov = curve_fit(func, x, yn, p0=[510, 0.00005, 490])

plt.figure()
plt.plot(x, yn, 'ko', label="Original Noised Data")
plt.plot(x, func(x, *popt), 'r-', label="Fitted Curve")
plt.legend()
plt.show()

print(popt)
print(pcov)
