import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')
sns.set_style('whitegrid')
sns.boxplot(x='Pclass', y='Age', data=titanic)
plt.show()