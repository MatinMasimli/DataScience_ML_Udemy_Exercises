import numpy as np
import matplotlib.pyplot as plt

'''
    Exercise 1
'''

x = np.arange(0, 100)
print("x values: ", x)

y = x * 2
print("y values: ", y)

z = x**2
print("z values: ", z)

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(x, y)

plt.xticks(np.arange(0, 120, step=20))
plt.yticks(np.arange(0, 250, step=50))

ax.set_xlim(0, 100)
ax.set_ylim(0, 200)

ax.set_title('title')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()
plt.close(fig)

