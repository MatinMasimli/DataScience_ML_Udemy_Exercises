import pandas as pd

ecom = pd.read_csv('Ecommerce Purchases.csv')

print(ecom.head())
print('**********\n')

print(ecom.info())
print('++++++++++\n')

print(ecom['Purchase Price'].mean())
print('$$$$$$$$$$\n')

print(ecom['Purchase Price'].max())
print('@@@@@@@@@@\n')

print(ecom['Purchase Price'].min())
print('&&&&&&&&&&\n')

print(ecom[ecom['Language'] == 'en'].count())
print('**********\n')

print(ecom[ecom['Job'] == 'Lawyer'].info())
print('%%%%%%%%%%\n')

print(ecom['AM or PM'].value_counts())
print('!!!!!!!!!!\n')

print(ecom['Job'].value_counts().head())
print('**********\n')

print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])
print('++++++++++\n')

print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])
print('@@@@@@@@@@\n')

print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())
print('----------\n')

print('Did not understand this question !!!')
#print(ecom[ecom['CC Exp Date'] == '2025'].sum())
print('++++++++++\n')

def divide_title(title):
    listOfWords = title.lower().split('@')
    return listOfWords[1]

print(ecom['Email'].apply(lambda x: divide_title(x)).value_counts().head())
print('&&&&&&&&&\n')

