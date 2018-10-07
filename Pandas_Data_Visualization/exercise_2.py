import pandas as pd
import matplotlib.pyplot as plt

datafile3 = pd.read_csv('df3.csv')
plt.style.use('ggplot')
datafile3['a'].plot.hist(bins=50)
plt.show()
