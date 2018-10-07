import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datafile3 = pd.read_csv('df3.csv')
sns.set_style('whitegrid')
datafile3 = datafile3.ix[:30,:]
datafile3.plot.area(alpha=0.4)
plt.show()
