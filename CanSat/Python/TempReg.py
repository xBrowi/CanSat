import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter
from scipy.stats import linregress

with open("C:/Users/augus/Desktop/CanSat/CanSat/testdata.txt") as f:
    lines = f.readlines()

k=0.16
k1=1/2000
k4=0.000000002

time=[]
ntcTempRaw=[]
bmpTemp=[]
bmpTryk=[]
bmpAlt=[]
lys=[]

for i in range(700, len(lines)-40, 1):
    x = lines[i].split()
    time.append(int(x[1])-70000)
    ntcTempRaw.append(int(x[2]))
    bmpTemp.append(float(x[3]))
    #bmpTryk.append(float(x[4]))
    #bmpAlt.append(float(x[5]))
    #lys.append(float(x[6]))

def ItoT(i):
    R = 10000 / (i*6.144/5 / (32767 - i*6.144/5))
    A = 0.003354016
    B = 0.000256985
    C = 0.000002620131
    D = 0.00000006383091
    return (1 / (A + B * (np.log(R / 10000)) + C * pow(np.log(R / 10000), 2) + D * pow(np.log(R / 10000), 3)))

def PtoH(P):
    A=np.float64(102.3)
    B=np.float64(273.15+15.5)
    C=np.float64(32)
    G=np.float64(9.82)
    M=np.float64(0.02897)
    R=np.float64(8.31446261815324)
    return (G*M*C-np.log(P/A)*R*B)/(G*M)


w = 24

ntcTemp = ItoT(np.array(ntcTempRaw))
ntcTempSavgol = savgol_filter(ntcTemp,20,1)
RealTime = np.array(time)/1000
RealTimeTemp = RealTime+w/10
RealTemp1=[]
RealTemp2=[]
ntcTempSlope=[]
RegTemp=[]

for i in range(0, len(ntcTemp)-w,1) :
    slope=linregress(RealTime[i:i+w],ntcTempSavgol[i:i+w])[0]
    ntcTempSlope.append(slope)
    RegTemp.append(ntcTemp[i+round(w/2)])

#for i in range(0, len(ntcTemp)-w,1) :
    #slope=linregress(RealTime[i:i+w],ntcTemp[i:i+w])[0]
    #RealTemp1.append((slope)/(k+k1*((ntcTemp[i]+ntcTemp[i+w])/2))+(ntcTemp[i]+ntcTemp[i+w])/2)

#for i in range(0, len(ntcTemp)-w,1) :
    #slope=np.float64(linregress(RealTime[i:i+w],ntcTempSavgol[i:i+w])[0])
    #RealTemp2.append(np.float64(1.1900790724238090551)*(np.float64(0.49853623242466805265)*np.float64(ntcTempSavgol[i+5])**4 + np.float64(2.9664876852680471781)*(10**8)*slope + np.float64(6.3626381837338645147)*(10**3))**(1/4))


RegTempSavgol = savgol_filter(RegTemp,20,1)


u=0
s=0


#plt.plot(RealTimeTemp[u:len(ntcTemp)-w], ntcTempSavgol[u:len(ntcTemp)-w], label='ntcTempSavgol')
#plt.plot(RealTimeTemp[u:len(ntcTemp)-w], ntcTemp[u:len(ntcTemp)-w], label='ntcTemp')
#plt.plot(RealTimeTemp[u:len(ntcTemp)-w], RealTemp1[u:], label='Omgivelser1')
#plt.plot(RealTimeTemp[u:len(ntcTemp)-w], RealTemp2[u:], label='Omgivelser2')
#plt.plot(RealTimeTemp[u:len(ntcTemp)-w], savgol_filter(RealTemp2[u:],15,1)-273.15, label='Model')
#plt.plot(RealTime[u:],np.array(ntcTemp[u:])-273.15, label='NTC', color='orange')
#plt.plot(RealTime[u:],np.array(bmpTemp[u:]), label='bmp', color='green')
#plt.plot(RealTime[u:], np.array(bmpAlt[u:])+250, label="bmpAlt")
plt.plot(RealTime[u:],ntcTempSavgol[u:]-273.15, label='SensorFix', color='green')
#plt.plot(RealTimeTemp[u:len(ntcTemp)-w],ntcTempSlope[u:], label='dT/dt')
plt.legend()
plt.xlabel('Tid [s]')
plt.ylabel('Temperatur [$\circ$C]')
plt.grid()
plt.show()
'''
plt.scatter(bmpAlt[u:len(ntcTemp)-w],savgol_filter(RealTemp2[u:],15,1)-273.15,s=10, label="model")
plt.scatter(bmpAlt[u:],np.array(ntcTemp[u:])-273.15,s=10, label="ntc")
#plt.scatter(bmpAlt[u:],np.array(bmpTemp[u:]),s=10, label="bmp")
plt.legend()
plt.xlabel('Højde [m]')
plt.ylabel('Temperatur [$\circ$C]')
plt.grid()
plt.show()
'''

'''

#res=linregress(RealTime[u:s], PtoH(np.array(bmpTryk)/10)[u:s])
#print(res)
#plt.plot(RealTime[u:s], res.intercept + res.slope*RealTime[u:s], 'r', label='fitted line')
plt.plot(RealTime[u:s], np.array(lys)[u:s], label="BH1750")
#plt.plot(RealTime[u:s], PtoH(np.array(bmpTryk)/10)[u:s], label="Model")
plt.legend()
plt.xlabel('Tid [s]')
plt.ylabel('Belysningsstyrke [lx]')
plt.grid()
plt.show()
'''


o=0

'''plt.scatter(RegTemp[o:],ntcTempSlope[o:],label="aaaaaa")

plt.ylabel('dT/dt [K/s]')
plt.xlabel('Temp [K]')
plt.show()'''




def func(T, k, c):
    return -k*(T-21.78156885-273.15)-c*((T)**4-(21.78156885+273.15)**4)


popt, pcov = curve_fit(func, np.array(RegTemp[o:]), ntcTempSlope[o:], p0=[10, 0])



plt.plot(np.array(RegTemp[o:]), func(np.array(RegTemp[o:]), *popt), 'r-', label="Model")
plt.scatter(RegTemp[o:],ntcTempSlope[o:],label="Måledata")
plt.legend()
plt.ylabel('dT/dt [K/s]')
plt.xlabel('Temp [K]')
plt.grid()
plt.show()
print(popt)

print(RegTemp[100])
