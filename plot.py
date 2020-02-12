import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,10)
y = x*x*x
plt.plot(x, y, "r--")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("my plot")

plt.plot(x, x, "g-")
plt.axis([-1, 10, -5, 45])
plt.show()