import numpy as np
import matplotlib.pyplot as plt

'''
    Exercise 4
'''

x = np.arange(0, 100)
y = x * 2
z = x**2

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 3))

ax[0].set_xlabel('X')
ax[0].set_ylabel('Y')
ax[0].set_xlim(0, 100)
ax[0].set_ylim(0, 200)
ax[0].plot(x, y, lw=3, color='blue')
plt.xticks(np.arange(0, 120, step=20))
plt.yticks(np.arange(0, 250, step=50))

ax[1].set_xlabel('X')
ax[1].set_ylabel('Z')
ax[1].set_xlim(0, 100)
ax[1].set_ylim(0, 10000)
ax[1].plot(x, z, lw=3, ls = '--',color='red')
plt.xticks(np.arange(0, 120, step=20))
plt.yticks(np.arange(0, 12000, step=2000))

plt.show()
