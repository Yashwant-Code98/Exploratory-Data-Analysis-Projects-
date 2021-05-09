import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

titanic = pd.read_csv('titanic.csv')

print(titanic.head())

print(titanic['Survived'].value_counts())

# make a bar plot for passenger who survived

plt.figure(figsize=(8,5))
plt.bar(list(titanic['Survived'].value_counts().index),list(titanic['Survived'].value_counts()),color=['green','orange'])
plt.show()


# Sex Wise who survived in titanic

plt.figure(figsize=(8,5))
plt.bar(list(titanic['Sex'].value_counts().keys()),list(titanic['Survived'].value_counts()),color=['brown','red'])
plt.show()

print(titanic['Sex'].value_counts())

plt.figure(figsize=(8,5))
plt.bar(list(titanic['Sex'].value_counts().index),list(titanic['Sex'].value_counts()),color=['blue','c'])
plt.show()


print(titanic['Age'].value_counts())

plt.figure(figsize=(8,5))
plt.hist(titanic['Age'],color='red',bins=50)
plt.show()

