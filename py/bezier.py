from numpy import linspace as lin  # linespace
from scipy.special import comb  # binomial coefficient
import matplotlib.pyplot as plt  # plotting

cpx = [0.0, 0.5, 2.0]
cpy = [0.0, 3.0, 0.0]

t = lin(0, 1, 100)  # Input as 100 floats between 0 and 1
num = 2  # The degree 0 indexed

# returns the value from the Bernstein basis function at the point x
def bern(i, n, x):
    return comb(n, i) * x ** i * (1 - x) ** (n-i)

# Generalized De Casteljau's Explicit formula 
def f(a, t):
    ret = 0
    for i in range(num + 1):
        ret += a[i] * bern(i, num, t)
    return ret

def x(t: float) -> float: return f(cpx, t) # implemented on X's control points
def y(t: float) -> float: return f(cpy, t) # implemented on Y's control points

plt.plot([x(i) for i in t], [y(i) for i in t]) # plots X and Y
plt.plot(cpx, cpy, 'ro') # plots the control points
plt.plot(cpx, cpy, 'r:') # plots lines between control points
plt.show()