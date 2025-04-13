import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# lists
x=[1,2,3,4]
y=[10,20,60,90]
# plt.plot(x,y)
# plt.show()


# line plot  -->used for to recognize the trends over time 
'''plt.plot([1,2,3], [10,20,30], label="Trends")
plt.title("Line Plot")
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
plt.legend()
plt.show()'''

# Bar Chart --->used for showcase categorical data 
'''categories=["A", "B", "C"]
values=[10,2,7]
plt.bar(categories, values, color="pink")
plt.title("Bar Chart")
plt.show(
)'''

# Histogram --->shows the distribution of the dataset
'''data=[1,2,2,3,5,5,6,6,6]
plt.hist(data, bins=4, color="silver",  edgecolor="black" )
plt.title("Histogram")
plt.show()
'''

'''
# scattered plot -->use in AI project use to visualize the relationship with two continous variable
x=[1,2,3,4]
y=[10,11,28,19]
plt.scatter(x,y, color="Red")
plt.show() 

'''

df = sns.load_dataset("tips")  # Load the "tips" dataset
print(df.head())  # Display first 5 rows