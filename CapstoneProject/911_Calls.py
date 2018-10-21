import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('911.csv')
print(df.info())

print('\n*********\n')

print(df.head())

print('\n+++++++++\n')

print(df['zip'].value_counts().head(5))

print('\n#########\n')

print(df['twp'].value_counts().head(5))

print('\n$$$$$$$$$\n')

print(df['title'].nunique())

print('\n@@@@@@@@@\n')

df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])
print(df.head())

print('\n#########\n')

print(df['Reason'].value_counts())

print('\n$$$$$$$$$\n')

print('\nCountplot of 911 calls by Reason\n')
sns.set(style="whitegrid")
sns.countplot(x="Reason", data=df).set_title("Count of Reasons")
plt.show()

print('\n*********\n')

print(type(df['timeStamp'].iloc[0]))

print('\n+++++++++\n')

print('\nConvert from strings to DateTime objects\n')
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

print('\n@@@@@@@@@\n')

df['Hour'] = df['timeStamp'].apply(lambda x: x.hour)
df['Month'] = df['timeStamp'].apply(lambda x: x.month)
df['Day of Week'] = df['timeStamp'].apply(lambda x: x.dayofweek)
print(df.head())

print('\n#########\n')

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
print(df.head())

print('\n%%%%%%%%%\n')

print('\nCreate a countplot of the Day of Week column\n')
sns.set_style('whitegrid')
sns.countplot(x='Day of Week', hue="Reason", data=df)
plt.show()

print('\n$$$$$$$$$\n')

print('\nCreate a countplot for Month column\n')
sns.set_style('whitegrid')
sns.countplot(x='Month', hue="Reason", data=df)
plt.show()

print('\n^^^^^^^^^^\n')

print('\nCreate an object called byMonth\n')
byMonth = df.groupby('Month').count()
print(byMonth.head())
print(byMonth.info())

print('\n!!!!!!!!!!\n')

print(df.iloc[0])
print('\n~~~~~~~~~~~\n')
print(byMonth.iloc[0])

print('\n{}{}{}{}{}{}{}{}\n')

print('\nCreate a simple plot off of the dataframe indicating the count of calls per month\n')
byMonth['timeStamp'].plot()
plt.show()

print('\n&&&&&&&&&&&&&&&\n')

print('\nUse lmplot() to create a linear fit\n')
sns.lmplot(x='Month', y='twp', data=byMonth.reset_index())
plt.show()

print('\n---------------\n')

df['Date'] = df['timeStamp'].apply(lambda x: x.date())
print(df.head())

print('\n**************\n')

print('\nGroupby the Date column with count() and create a plot of counts of 911 calls\n')
byDate = df.groupby('Date').count()
byDate['addr'].plot()
plt.show()

print(byDate.info())
print('\n++++++++++++++\n')
print(byDate.head())

print('\n##############\n')

print('\nCreate 3 separate plots representing a Reason for the 911 call\n')

trafficGrouped = df[df['Reason'] == 'Traffic'].groupby('Date').count()
trafficGrouped['Reason'].plot()
plt.title('Traffic')
plt.show()

trafficGrouped = df[df['Reason'] == 'Fire'].groupby('Date').count()
trafficGrouped['Reason'].plot()
plt.title('Fire')
plt.show()

trafficGrouped = df[df['Reason'] == 'EMS'].groupby('Date').count()
trafficGrouped['Reason'].plot()
plt.title('EMS')
plt.show()

print('\n$$$$$$$$$$$\n')

dayHour = df.groupby(by=['Day of Week','Hour']).count()['twp'].unstack()
print(dayHour.head())

print('\n@@@@@@@@@@\n')

print('\nCreate a HeatMap using new dayHour dataframe\n')
plt.figure(figsize=(12,6))
sns.heatmap(dayHour)
plt.show()

print('\n!!!!!!!!!!\n')

print('\nCreate a clustermap using new dayHour dataframe\n')
sns.clustermap(dayHour, cmap='viridis')
plt.show()

print('\n############\n')

dayMonth = df.groupby(by=['Day of Week','Month']).count()['twp'].unstack()
print(dayMonth.head())

print('\n************\n')

print('\nCreate a HeatMap using new dayMonth dataframe\n')
plt.figure(figsize=(12,6))
sns.heatmap(dayMonth)
plt.show()

print('\n++++++++++++\n')

print('\nCreate a clustermap using new dayMonth dataframe\n')
sns.clustermap(dayMonth, cmap='viridis')
plt.show()




