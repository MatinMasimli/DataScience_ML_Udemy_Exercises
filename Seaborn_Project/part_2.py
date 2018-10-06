import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')
sns.set_style('whitegrid')
sns.distplot(titanic['Fare'], kde=False, color = 'red')
plt.xlim(0, 600)
plt.ylim(0, 500)
plt.show()