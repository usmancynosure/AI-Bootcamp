# titanic data set 
# https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# load the data-set
url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# inspect the data 
# print(df.info())  ------->all the basic infomation(how many values are missing )
# print(df.describe())   ---->this can calculate some basic statistical values like standard dev, max,min values


#handle missing data 
df['Age']=df['Age'].fillna(df['Age'].median())
df['Embarked']= df['Embarked'].fillna(df['Embarked'].mode()[0]) 
 

# Remove the duplications
df=df.drop_duplicates()


# Filtering the data --> passenger in first class
first_class= df[df['Pclass'] == 1]
# print("First class passenger \n ", first_class.head())


# DIsplay a bar chart ---> survival rate by classs
# ()--->the class that i want to display
survival_by_class= df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar", color="silver")
plt.title("Survival Rate by Class")
plt.ylabel("survival rate")
plt.xlabel("classes")
plt.show()
# print(survival_by_class)


# Create Histogram for Age Distribution
sns.histplot(df['Age'], kde=True, bins=20, color="Navy")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("frequency")
plt.show()


# Scattered plot
plt.scatter(df['Age'], df['Fare'], alpha=0.5, color='green')
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()


