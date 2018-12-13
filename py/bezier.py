from numpy import linspace as lin  # linespace
from scipy.special import comb  # binomial coefficient
import matplotlib.pyplot as plt  # plotting

cpx = [0.0, 0.5, 2.0, 1.5] # control point x coordinates
cpy = [0.0, 3.0, 0.0, 3.0] # control point y coordinates

t = lin(0, 1, 100)  # 100 sample inputs between 0 and 1
num = 3  # degree 0 indexed

# returns the value from the Bernstein basis function at the point x
def bern(i, n, t):
    return comb(n, i) * t ** i * (1 - t) ** (n-i)

# Generalized De Casteljau's Explicit formula 
def f(a, t):
    ret = 0
    for i in range(num + 1):
        ret += a[i] * bern(i, num, t)
    return ret

def x(t): return f(cpx, t) # implemented on X's control points
def y(t): return f(cpy, t) # implemented on Y's control points

plt.plot([x(i) for i in t], [y(i) for i in t]) # plot bezier curve
plt.plot(cpx, cpy, 'ro') # plot control points
plt.plot(cpx, cpy, 'r:') # graph lines between control points
for i in range(num+1):
    # label control points
    plt.text(cpx[i]+0.05, cpy[i]+0.05, 'P{}'.format(i))
plt.title('Bezier') # title
plt.show() # display graphs