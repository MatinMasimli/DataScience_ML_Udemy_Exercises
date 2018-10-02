import numpy as np
import matplotlib.pyplot as plt

'''
    Exercise 2
'''

x = np.arange(0, 100)
y = x * 2
z = x**2

fig = plt.figure()

ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 200)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.plot(x, y, 'r')

plt.xticks(np.arange(0, 120, step=20))
plt.yticks(np.arange(0, 250, step=50))

ax2 = fig.add_axes([0.2, 0.5, 0.2, 0.2])
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 200)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.plot(x, y, 'r')

plt.xticks(np.arange(0, 120, step=20))
plt.yticks(np.arange(0, 250, step=50))

plt.show()
plt.close(fig)