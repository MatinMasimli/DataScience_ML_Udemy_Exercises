import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')
sns.heatmap(titanic.corr(), cmap='coolwarm', vmin=-1, vmax=1, annot=True)
plt.title('titanic.corr()')
plt.show()