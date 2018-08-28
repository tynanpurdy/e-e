import matplotlib.pyplot as plt
import numpy as np

cpx = [1.0, 3.0, 6.0, 8.0]
cpy = [1.0, 9.0, 6.0, 1.0]
x   = []
y   = []

# uncomment the section with the order of polynomial desired.
# remember to adjust the size of the control point coordinate arrays
'''
# 1st order Bernstein polynomial
#P1 = p1 * (1-t) + p2 * t
def x1(t):
    x = cpx[0] * (1-t)  \
    +  cpx[1] * t
    return x
def y1(t):
    y = cpy[0] * (1-t)  \
    +  cpy[1] * t
    return y
'''
'''
# 2nd order Bernstein polynomial
#P2 = p1     * (1-t)**2  +  2 * p2     * t * (1-t)  +  p3     * t**2
def x2(t):
    x = cpx[0] * (1-t)**2  \
    +  2 * cpx[1] * t * (1-t)  \
    +  cpx[2] * t**2
    return x
def y2(t):
    y = cpy[0] * (1-t)**2  \
    +  2 * cpy[1] * t * (1-t)  \
    +  cpy[2] * t**2
    return y
'''

# 3rd order Bernstein polynomial
#P3 = p1 * (1-t)**3 + 3 * p2 * t * (1-t)**2 + 3 * p3 * (1-t) * t**2 + p4 * t**3
def x3(t):
    x = cpx[0] * (1-t)**3  \
    +  3 * cpx[1] * t * (1-t)**2  \
    +  3 * cpx[2] * (1-t) * t**2  \
    +  cpx[3] * t**3
    return x
    
def y3(t):
    y = cpy[0] * (1-t)**3  \
    +  3 * cpy[1] * t * (1-t)**2  \
    +  3 * cpy[2] * (1-t) * t**2  \
    +  cpy[3] * t**3
    return y


for t  in np.linspace(0, 1, 100):
    xarray = x3(t)      # match with chosen functions from above
    x.append(xarray)
    yarray = y3(t)      # match with chosen functions from above
    y.append(yarray)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x, y)
ax.plot(cpx, cpy, 'r--')
ax.plot(cpx, cpy, 'ro')

plt.grid()
plt.xlim(0, 10)
plt.ylim(0, 10)

# label control points. comment out lines referencing cps that aren't being used
ax.text( cpx[0]+0.1, cpy[0]+0.1, 'P0')
ax.text( cpx[1]-0.1, cpy[1]+0.2, 'P1')
ax.text( cpx[2]+0.1, cpy[2]+.01, 'P2')
ax.text( cpx[3]-0.1, cpy[3]+0.2, 'P3')

ax.set_aspect("equal")
plt.title('Bezier Curve')
plt.draw()
plt.show()