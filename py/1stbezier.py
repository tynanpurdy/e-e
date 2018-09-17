import matplotlib.pyplot as plt
import numpy as np

cpx = [1.0, 3.0]
cpy = [1.0, 9.0]
x   = []
y   = []

# 1st order Bernstein polynomial
#P1 = p1 * (1-t) + p2 * t
def x(t):
    x = cpx[0] * (1-t)  \
    +  cpx[1] * t
    return x
def y(t):
    y = cpy[0] * (1-t)  \
    +  cpy[1] * t
    return y

for t  in np.linspace(0, 1, 100):
    xarray = x(t)
    x.append(xarray)
    yarray = y(t)     
    y.append(yarray)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.plot(cpx, cpy, 'ro')

plt.grid()
plt.xlim(0, 10)
plt.ylim(0, 10)

# label control points
ax.text( cpx[0]+0.1, cpy[0]+0.1, 'P0')
ax.text( cpx[1]-0.1, cpy[1]+0.2, 'P1')

ax.set_aspect("equal")
plt.title('1st Order B\'ezier Curve')
plt.draw()
plt.show()