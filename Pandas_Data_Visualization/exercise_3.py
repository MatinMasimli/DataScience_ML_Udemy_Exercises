import pandas as pd
import matplotlib.pyplot as plt

datafile3 = pd.read_csv('df3.csv')
datafile3[['a', 'b']].plot.box()
plt.show()