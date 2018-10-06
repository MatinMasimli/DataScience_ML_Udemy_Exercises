import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('train.csv')
sns.set_style('whitegrid')
mygraph = sns.JointGrid(x = 'Fare', y = 'Age', data=titanic)
mygraph = mygraph.plot_joint(plt.scatter)
mygraph = mygraph.plot_marginals(sns.distplot, kde=False)
plt.show()
