import numpy as np
from matplotlib import pyplot

x = 67.3
z = [1.71, 1.74, 1.72, 1.76, 1.78, 1.72]
z = [i * 2 for i in z]
m = [i + 1 for i in range(6)]
print(m, z)


coeffs = np.polyfit(m, z, 1)
k = coeffs[0]
b = coeffs[1]
line_points = [k * number + b for number in m]
pyplot.plot(m, line_points, color='b')
pyplot.legend(["b = 3.5 мм "])
pyplot.scatter(m, z, color="r")
print(k)

pyplot.grid()
pyplot.xlabel("$m$")
pyplot.ylabel("$2\\xi_m, мм $")
pyplot.title("$График$ $зависимости$ $2\\xi_m$ $oт$ $m$")
pyplot.ylim([2.3, 4])
# pyplot.show()
pyplot.savefig("1.pdf")


# pyplot.grid()
# pyplot.xlabel("$t, с$")
# pyplot.ylabel("$ln\\frac{U}{U_0}$")
# pyplot.legend(["40 торр", "92 торр", "144 торр", "196 торр", "250 торр"])
# pyplot.title("$График$ $зависимости$ $ln\\frac{U}{U_0}$ $oт$ $t$")
#
# # pyplot.show()
# pyplot.savefig("Laba_2_2_1")
# print(k, k_247, k_194, k_146, k_97)

# d = [10.392, 4.598, 2.895, 2.361, 1.645, 0.705]
# p = [1/40, 1/97, 1/146, 1/194, 1/247, 1/742]
#
# d_1 = [0.705]
# p_1 = [1/742]
#
# pyplot.scatter(p_1, d_1, color='g')
# pyplot.scatter(p, d, color='r')
# pyplot.scatter(p_1, d_1, color='g')
#
# coeffs = np.polyfit(p, d, 1)
# k = coeffs[0]
# b = coeffs[1]
# line_points = [k * number + b for number in p]
# pyplot.plot(p, line_points, color='b')
#
# pyplot.grid()
# pyplot.xlabel('$\\frac{1}{P}, торр^{-1}$')
# pyplot.ylabel("$D, \\frac{см^{2}}{c}$")
# pyplot.legend(["$D_{aтм} = 0, 705 \\frac{см^{2}}{c}$"])
# pyplot.title("График зависимости $D$ от $\\frac{1}{P}$")
#
# # pyplot.show()
# # print(k)
# pyplot.savefig("Laba_2_2_1_plot_2")