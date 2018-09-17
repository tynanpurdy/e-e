import matplotlib.pyplot as plt
import numpy as np

cpx = [1.0, 3.0, 6.0]
cpy = [1.0, 9.0, 6.0]
x   = []
y   = []


# 2nd order Bernstein polynomial
#P2 = p1     * (1-t)**2  +  2 * p2     * t * (1-t)  +  p3     * t**2
def x(t):
    x = cpx[0] * (1-t)**2  \
    +  2 * cpx[1] * t * (1-t)  \
    +  cpx[2] * t**2
    return x
def y(t):
    y = cpy[0] * (1-t)**2  \
    +  2 * cpy[1] * t * (1-t)  \
    +  cpy[2] * t**2
    return y

for t  in np.linspace(0, 1, 100):
    xarray = x(t)
    x.append(xarray)
    yarray = y(t)
    y.append(yarray)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.plot(cpx, cpy, 'r--')
ax.plot(cpx, cpy, 'ro')

plt.grid()
plt.xlim(0, 10)
plt.ylim(0, 10)

# label control points
ax.text( cpx[0]+0.1, cpy[0]+0.1, 'P0')
ax.text( cpx[1]-0.1, cpy[1]+0.2, 'P1')
ax.text( cpx[2]+0.1, cpy[2]+.01, 'P2')

ax.set_aspect("equal")
plt.title('2nd Order B\'ezier Curve')
plt.draw()
plt.show()