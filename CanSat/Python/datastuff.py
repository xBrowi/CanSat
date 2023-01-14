import matplotlib.pyplot as plt
import numpy as np

with open('D:\data.txt') as f:
    lines = f.readlines()

time=[]
ntcTempRaw=[]
bmpTemp=[]
bmpTryk=[]
bmpAlt=[]

for i in range(550, len(lines), 1):
    time.append(int(lines[i].split()[1])-55000)
    ntcTempRaw.append(int(lines[i].split()[2]))
    """bmpTemp.append(float(lines[i].split()[3]))
    bmpTryk.append(float(lines[i].split()[4]))
    bmpAlt.append(float(lines[i].split()[5]))"""

plt.plot(time, ntcTempRaw)
plt.show()
from scipy.optimize import curve_fit


def fit_func(x, k):
    return (ntcTempRaw[0]-490)*pow(np.e, -k*x)+490

params = curve_fit(fit_func, time, ntcTempRaw)

[k] = params[0]


print(k)