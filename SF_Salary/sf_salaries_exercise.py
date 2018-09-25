import pandas as pd

sal = pd.read_csv('SF_Salary/Salaries.csv')

print(sal.head())
print("++++++++++\n")

print(sal.info())
print('*********\n')

sal['BasePay'] = pd.to_numeric(sal['BasePay'], errors='coerce')
sal.dropna()
avgBasePay = sal["BasePay"].mean(axis=0)
print(avgBasePay)
print('&&&&&&&&&&\n')

sal['OvertimePay'] = pd.to_numeric(sal['OvertimePay'], errors='coerce')
sal.dropna()
minOverTimePay = sal["OvertimePay"].max()
print(minOverTimePay)
print('$$$$$$$$$\n')

empName_jobTitle = sal[['EmployeeName', 'JobTitle']]
print(empName_jobTitle[empName_jobTitle['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
print('%%%%%%%%%\n')

empName_jobTitle = sal[['EmployeeName', 'TotalPayBenefits']]
print(empName_jobTitle[empName_jobTitle['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])
print('~~~~~~~~~\n')

sal['TotalPayBenefits'] = pd.to_numeric(sal['TotalPayBenefits'], errors='coerce')
sal.dropna()
maxTotalPay = sal['TotalPayBenefits'].max()
highestPaidEmp = sal[sal['TotalPayBenefits'] == maxTotalPay]
print(highestPaidEmp)
print('&&&&&&&&\n')

sal['TotalPayBenefits'] = pd.to_numeric(sal['TotalPayBenefits'], errors='coerce')
sal.dropna()
minTotalPay = sal['TotalPayBenefits'].min()
lowestPaidEmp = sal[sal['TotalPayBenefits'] == minTotalPay]
print(lowestPaidEmp)
print('@@@@@@@@@\n')

print('Different solution method for the question above!!!')
print(sal.loc[sal['TotalPayBenefits'].idxmin()])
print('@@@@@@@@@\n')

groupForYear = sal.groupby('Year').mean()
print(groupForYear['BasePay'])
print('!!!!!!!!!\n')

allJobTitles = list(sal['JobTitle'].unique())
print(len(allJobTitles))
print('*********\n')

print('Different solution method for the question above!!!')
print(sal['JobTitle'].nunique())
print('#########\n')

commonJobs = sal['JobTitle'].value_counts()
print(commonJobs.head())
print('&&&&&&&&&\n')

print('Not done in 2013')
print('%%%%%%%%%\n')
listOfJobTitles = sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)
print(listOfJobTitles)
print('!!!!!!!!!\n')


def divide_title(title):
    listOfWords = title.lower().split()
    if 'chief' in listOfWords:
        return True
    return False

print(sal['JobTitle'].apply(lambda x: divide_title(x)).sum())
print('@@@@@@@@@\n')

'''
print('Different solution method for the question above!!!')

resultList = []
def find_chief(title):
    listOfWords = title.lower().split()
    if 'chief' in listOfWords:
        resultList.append(title)

print(sal['JobTitle'].apply(lambda x: find_chief(x)))
'''
