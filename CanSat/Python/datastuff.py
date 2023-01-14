import matplotlib.pyplot as plt
import numpy as np

with open('D:\LOG00014.txt') as f:
    lines = f.readlines()

time=[]
ntcTempRaw=[]
bmpTemp=[]
bmpTryk=[]
bmpAlt=[]

for i in range(0, len(lines), 1):
    time.append(int(lines[i].split()[1]))
    ntcTempRaw.append(int(lines[i].split()[2]))
    bmpTemp.append(float(lines[i].split()[3]))
    bmpTryk.append(float(lines[i].split()[4]))
    bmpAlt.append(float(lines[i].split()[5]))

plt.plot(time, bmpTemp)
plt.show()