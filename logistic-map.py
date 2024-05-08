

import numpy as np
import matplotlib.pyplot as plt

def logistic_map(r, x0, n):
    """Compute the logistic map
    x_n+1 = r * x_n * (1-x_n) where x_n+1 is the next point in the series
    """
    results = [x0]
    for _ in range(n-1):
        x = results[-1]
        next_x = r * x * (1 - x)
        results.append(next_x)
    return results

# Parameters
n = 1000  # Number of iterations for each value of r
r_values = np.linspace(2.5, 4.0, 1000)  # Range of growth rates
x0 = 0.5  # Initial population

# Generate bifurcation diagram
bifurcation_data = []
for r in r_values:
    population = logistic_map(r, x0, n)[-500:]  # Discard transient
    bifurcation_data.extend([[r, x] for x in population])

bifurcation_data = np.array(bifurcation_data)

# Plot bifurcation diagram
plt.figure(figsize=(10, 6))
plt.scatter(bifurcation_data[:, 0], bifurcation_data[:, 1], s=0.1, marker='.')
plt.xlabel('Growth Rate (r)')
plt.ylabel('Population')
plt.title('Bifurcation Diagram of the Logistic Map')
plt.show()
