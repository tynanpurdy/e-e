from numpy import linspace as lin  # linespace
from scipy.special import comb  # binomial coefficient
import matplotlib.pyplot as plt  # plotting

x = lin(0, 1, 100)  # Input as 100 floats between 0 and 1
num: int = 10  # The degree

# returns the value from the Bernstein basis function at the point x
def bern(i: int, n: int, x: float) -> float:
    return comb(n, i) * x ** i * (1 - x) ** (n-i)

# Iterates through all of the functions for the degree
for c in range(num + 1):
    # Plots all of the functions 
    plt.plot(x, [bern(c, num, i) for i in x])

plt.title("Bernstein Basis Functions")  # Title
plt.show()  # displays graphs