import numpy as np
from matplotlib import pyplot

F = [0.6, 0.6, 0.55, 0.6]
N = [100, 150, 225, 300]

K = [i for i in range(5)]
f = [0.64, 0.63, 0.62, 0.61, 0.61]

coeffs = np.polyfit(K, f, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in K]
pyplot.plot(K, line_points, color='b')
pyplot.scatter(K, f, color="r")
pyplot.legend(["$lim(F)$ = 0.6Н"])

# print(k)

pyplot.grid()
pyplot.xlabel("$K$")
pyplot.ylabel("$F, H$")
pyplot.title("$График$ $зависимости$ $F$ $oт$ $K$")
pyplot.ylim([0, 1])
pyplot.show()
# pyplot.savefig("F(K).pdf")


