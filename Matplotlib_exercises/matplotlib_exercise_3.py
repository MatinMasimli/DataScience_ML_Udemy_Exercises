import numpy as np
import matplotlib.pyplot as plt

'''
    Exercise 3
'''

x = np.arange(0, 100)
y = x * 2
z = x**2

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax1.set_ylim(0, 10000)
ax1.set_xlim(0, 100)
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax1.plot(x, z, 'r')

plt.yticks(np.arange(0, 12000, step=2000))
plt.xticks(np.arange(0, 120, step=20))


ax2 = fig.add_axes([0.2, 0.4, 0.3, 0.3])
ax2.set_xlim(20.0, 22.0)
ax2.set_ylim(30, 50)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.plot(x, y, 'r')
ax2.set_title('zoom')

plt.yticks(np.arange(30, 55, step=5))
plt.xticks(np.arange(20.0, 22.5, step=0.5))

plt.show()
