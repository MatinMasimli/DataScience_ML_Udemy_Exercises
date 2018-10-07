import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datafile3 = pd.read_csv('df3.csv')
sns.set_style('whitegrid')
datafile3['d'].plot.kde(ls='--', lw=5)
plt.show()