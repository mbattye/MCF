import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from helper_funcs import factors

data = np.genfromtxt("./intensity.dat")
print(data)
# print(np.shape(data))
# print(data.min())
# print(data.max())

for n in np.shape(data):
    print(f"Factors of {n}: {factors(n)}")

print(f"Factors of {data.max()}: {factors(data.max())}")

xticks = np.arange(0, np.shape(data)[0], 10)
# plt.xticks(xticks)
yticks = np.arange(0, np.shape(data)[1], 10)
# plt.yticks(yticks)
ax = sns.heatmap(data)
# ax.set_yticks(yticks)
# ax.set_yticklabels = yticks
ax.set_ylabel('Vertical pixel value')
ax.set_ylabel('Horizontal pixel value')

# , xticklabels=xticks, yticklabels=yticks)

plt.savefig("heatmap.png")
plt.show()