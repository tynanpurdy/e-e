from numpy import linspace as lin  # linespace
from scipy.special import comb  # binomial coefficient
import matplotlib.pyplot as plt  # plotting

x = lin(0, 1, 100)  # 100 sample inputs between 0 and 1
num = 4  # degree 0 indexed

# returns the value from the Bernstein basis function at the point x
def bern(i, n, t):
    return comb(n, i) * t ** i * (1 - t) ** (n-i)

# iterates through all of the functions for the degree
for c in range(num + 1):
    # plots all of the functions 
    plt.plot(x, [bern(c, num, i) for i in x])

plt.title("Bernstein Basis Functions")  # Title
plt.show()  # displays graphs