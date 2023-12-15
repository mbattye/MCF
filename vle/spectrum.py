import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt("./lambda.dat")

spec = data[142]

print(spec)

plt.plot(spec)
plt.show()