import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')
sns.set_style('darkgrid')
sns.countplot(x='Sex', data=titanic)
plt.show()