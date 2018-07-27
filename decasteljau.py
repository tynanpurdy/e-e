import matplotlib.pyplot as plt
import numpy as np

#t = np.linspace(0, 1, 100)

cpx = [0.0, 100, 0.0, 50]
cpy = [0.0, 0.0, 100, 50]
x   = []
y   = []

# 1st order Bernstein polynomial
#P1 = p1     * (1-t)  +  p2     * t
#x1 = cpx[0] * (1-t)  +  cpx[1] * t
#y1 = cpy[0] * (1-t)  +  cpy[1] * t

# 2nd order Bernstein polynomial
#P2 = p1     * (1-t)**2  +  2 * p2     * t * (1-t)  +  p3     * t**2
#x2 = cpx[0] * (1-t)**2  +  2 * cpx[1] * t * (1-t)  +  cpx[2] * t**2
#y2 = cpy[0] * (1-t)**2  +  2 * cpy[1] * t * (1-t)  +  cpy[2] * t**2

# 3rd order Bernstein polynomial
#P3 = p1     * (1-t)**3  +  3 * p2     * t * (1-t)**2  +  3 * p3     * (1-t) * t**2  +  p4     * t**3
def x3(t):
    x = cpx[0] * (1-t)**3  +  3 * cpx[1] * t * (1-t)**2  +  3 * cpx[2] * (1-t) * t**2  +  cpx[3] * t**3
    return x

def y3(t):
    y = cpy[0] * (1-t)**3  +  3 * cpy[1] * t * (1-t)**2  +  3 * cpy[2] * (1-t) * t**2  +  cpy[3] * t**3
    return y

for t in range(0, 100):
    xarray = x3(t)
    x.append(xarray)
    yarray = y3(t)
    y.append(yarray)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)

plt.title('Bezier Curve')
#plt.legend()
plt.show()

''' what you would do was have 4 variables for each coefficient in the cubic polynomial
    and then you would set them based on the formal shown
    and then you would interate through all of your t range get the x and y for your curve
    store those in an array and then display those arrays in matplot '''