import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
AutoMinorLocator)
import numpy as np
#библиотеки

#реализация выбора
print("1 - Вывести график на экран")
print("2 - Сохранить график на рабочий стол")
proverca = int(input())



lamb = 0.546

fi = [287, 288, 290, 292, 293, 294]
fi = [np.sin(i * np.pi / 180 ) - np.sin(np.pi / 4) for i in fi]
l = [4047, 4358, 4916, 5461, 5770, 6234]

#m = np.linspace(1, 6, 6);


#x2 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y2 = 4.5, 9, 16.5, 21, 27, 28.5, 30

#x3 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y3 = 9, 16.5, 27, 34.5, 40.5, 45, 46.5

#x4 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y4 = 10.5, 21, 33, 45, 52.5, 57, 60

#x5 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y5 = 12, 28.5, 43.5, 57, 66, 73.5, 78

#x6 = 206.06928,	397.01424,	579.65056,	745.15392,	884.7,	989.46448,	1044.576039
#y6 = 13.5, 33, 49.5, 66, 78, 88.5, 91.5



#xerr1=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842]) 
#yerr1=np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])

#xerr2=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686]) 
#yerr2=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])

#xerr3=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686]) 
#yerr3=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])

#xerr4=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686]) 
#yerr4=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])

#xerr5=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686]) 
#yerr5=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])

#xerr6=np.array([3.09104, 5.95521, 8.69476, 11.1773, 13.2705, 14.842, 15.6686]) 
#yerr6=np.array([1.5,	1.5,	1.5,	1.5,	1.5,	1.5,	1.5])




tochki1 = np.linspace(l[0], l[-1], 10000)
tochki2 = np.linspace(l[0], l[-1], 10000)
#tochki3 = np.linspace(x3[0], x3[-1], 10000)
#tochki4 = np.linspace(x4[0], x4[-1], 10000)
#tochki5 = np.linspace(x5[0], x5[-1], 10000)
#tochki6 = np.linspace(x6[0], x6[-1], 10000)


z1 = np.polyfit(l, fi, 1)
p1 = np.poly1d(z1)

#z3 = np.polyfit(x3, y3, 1) 
#p3 = np.poly1d(z3)  

#z4 = np.polyfit(x4, y4, 1) 
#p4 = np.poly1d(z4)  

#z5 = np.polyfit(x5, y5, 1) 
#p5 = np.poly1d(z5)  

#z6 = np.polyfit(x6, y6, 1) 
#p6 = np.poly1d(z6)  




fig, ax = plt.subplots(figsize=(10, 7))
if proverca == 1:
    fig, ax = plt.subplots(figsize=(10, 7))
else:
    fig, ax = plt.subplots(figsize=(10, 7), dpi = 600)
#для корректоного вывода на экан, не трогать


#plt.axis([16,32,0,4.6]) 
##обрезка координат


ax.set_title("Зависимость $sin \\varphi - sin \\psi$ от $\\lambda$", fontsize=16)                    #название графика
ax.set_xlabel("$\\lambda, A$", fontsize=14)                        #название оси х
ax.set_ylabel("$sin \\varphi - sin \\psi$", fontsize=14)     #название оси у
#названия и имена 



#ax.set_yscale('log')
#логарифмический масштаб для оси Y



ax.grid(which="major", linewidth=1.3)                               #мажорная сетка
ax.grid(which="minor", linestyle="--", color="gray", linewidth=0.5) #минорная сетка
#создаём сетку для графика


ax.plot(l, fi,"r.", markersize=8, label = 'k = 250 $\\cdot 10^3 м^{-1}$')
#ax.plot(m, r_l,"b.", markersize=8, label = 'Светлые кольца: k = 21.0нм' )
#ax.plot(x3, y3,"g.", markersize=8, label = 'Ток на образце 0.6 А' )
#ax.plot(x4, y4,"y.", markersize=8, label = 'Ток на образце 0.8 А')
#ax.plot(x5, y5,"k.", markersize=8, label = 'Ток на образце 1.0 А' )
#ax.plot(x6, y6,"m.", markersize=8, label = 'Ток на образце 1.2 А' )
#строительство графика на рисунке
ax.plot(tochki1, p1(tochki1), 'r--', label = '')
#ax.plot(tochki2, p2(tochki2), 'b--', label = '')
#ax.plot(tochki3, p3(tochki3), 'g--', label = '')
#ax.plot(tochki4, p4(tochki4), 'y--', label = '')
#ax.plot(tochki5, p5(tochki5), 'k--', label = '')
#ax.plot(tochki6, p6(tochki6), 'm--', label = '')


# ax.plot(m, p2(m), 'g--', label = 'Максимальный наклон кривой')
#ax.plot(x3, p3(x3), 'b--')
#в скобказ указываем точки графика для которого сторим линию тренда и функцию полинома
#строительство линии тренда
#ax.set_xticks(numpy.arange(0, 1000, 10))
#ax.set_yticks(numpy.arange(0, 1., 0.1))
ax.legend()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='major', length=10, width=1)
ax.tick_params(which='minor', length=5, width=1)
#строительство минорной и мажорной сетки

#ax.errorbar(x1, y1,
#xerr=xerr1,
#yerr=yerr1,
#fmt='.', color='red', markersize=5)

#ax.errorbar(x2, y2,
#xerr=xerr2,
#yerr=yerr2,
#fmt='.', color='blue', markersize=5)

#ax.errorbar(x3, y3,
#xerr=xerr3,
#yerr=yerr3,
#fmt='.', color='green', markersize=5)

#ax.errorbar(x4, y4,
#xerr=xerr4,
#yerr=yerr4,
#fmt='.', color='yellow', markersize=5)

#ax.errorbar(x5, y5,
#xerr=xerr5,
#yerr=yerr5,
#fmt='.', color='black', markersize=5)

#ax.errorbar(x6, y6,
#xerr=xerr6,
#yerr=yerr6,
#fmt='.', color='purple', markersize=5)






if proverca == 1:
    plt.show()
else:
    plt.savefig("sin.png")
