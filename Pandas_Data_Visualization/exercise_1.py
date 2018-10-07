import pandas as pd
import matplotlib.pyplot as plt

datafile3 = pd.read_csv('df3.csv')
datafile3.plot.scatter(x='a', y='b', s=30, figsize=(8, 3), c ='r', lw=1, edgecolors='black')
plt.show()


