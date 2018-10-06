import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')
sns.set_style('whitegrid')
g = sns.FacetGrid(titanic, col="Sex")
g = g.map(plt.hist, "Age")
plt.show()