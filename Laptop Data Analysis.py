import pandas  as pd
import matplotlib.pyplot as plt
import seaborn as sns


laptop = pd.read_csv('laptop.csv')

print(laptop.head())

# Laptop Inches by Product

print(laptop['Inches'].value_counts())

# top 5 inches of laptop
print(laptop['Inches'].value_counts()[0:5])

# Make a histogram to see the distribution of inches

plt.figure(figsize=(8,5))
plt.hist(laptop['Inches'],color='red',bins=20)
plt.show()

print(laptop['Memory Technology'].value_counts())

plt.figure(figsize=(8,5))
plt.bar(list(laptop['Memory Technology'].value_counts().index),list(laptop['Memory Technology'].value_counts()),color=['olive'])
plt.show()

print(laptop['Installed Memory'].value_counts())

# Top 5 laptop of high storage
print(laptop['Installed Memory'].value_counts()[0:5])

sns.histplot(laptop['Installed Memory'])
plt.show()

print(laptop['Processor speed'].value_counts())

# Top 5 laptops processor
print(laptop['Processor speed'].value_counts()[0:5])

plt.figure(figsize=(8,5))
plt.scatter(x = "Product", y = "Processor speed", data = laptop,color='olive')
plt.show()

print(laptop['Product'].value_counts())

# Top 5 Products of laptop Companies

print(laptop['Product'].value_counts()[0:5])


# Make a bar plot

plt.figure(figsize=(8,5))
plt.bar(list(laptop['Product'].value_counts().index[0:5]),list(laptop['Product'].value_counts()[0:5]),color=['green','blue','orange','olive','yellow'])
plt.show()

print(laptop['Infrared'].value_counts())


plt.figure(figsize=(5,5))
plt.bar(list(laptop['Infrared'].value_counts().keys()),list(laptop['Infrared'].value_counts()),color=['m','k'])
plt.show()

print(laptop['Bluetooth'].value_counts())

plt.figure(figsize=(8,5))
plt.bar(list(laptop['Bluetooth'].value_counts().index),list(laptop['Bluetooth'].value_counts()),color=['blue','red'])
plt.show()

print(laptop['Docking station'].value_counts())

sns.histplot(laptop['Docking station'],linewidth=3)
plt.show()

print(laptop['Port Replicator'].value_counts())

plt.figure(figsize=(7,7))
plt.pie(list(laptop['Port Replicator'].value_counts()),labels=list(laptop['Port Replicator'].value_counts().index),autopct='%0.1f%%')
plt.show()

print(laptop['Fingerprint'].value_counts())

plt.figure(figsize=(8,5))
plt.bar(list(laptop['Fingerprint'].value_counts().index),list(laptop['Fingerprint'].value_counts()),color=['pink'],linewidth=5)
plt.show()

print(laptop['Subwoofer'].value_counts())

plt.figure(figsize=(8,5))
plt.pie(list(laptop['Subwoofer'].value_counts()),labels=list(laptop['Subwoofer'].value_counts().index),autopct='%0.1f%%')
plt.show()

print(laptop['Operating system'].value_counts())


sns.histplot(laptop['Operating system'],color='darkgreen')
plt.show()

print(laptop['Warranty-Days'].value_counts())

plt.figure(figsize=(8,5))
plt.hist(laptop['Warranty-Days'])
plt.show()

print(laptop['Price'].value_counts)

plt.figure(figsize=(8,5))
plt.hist(laptop['Price'],color='olive',bins=20)
plt.show()

from sklearn.model_selection import train_test_split

x = laptop[['Inches']]
y = laptop[['Price']]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.65)

print(x_train.head())
print(x_test.head())
print(y_train.head())
print(y_test.head())

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
print(lr.fit(x_train,y_train))

lr.predict(x_test)
