import matplotlib.pyplot as plt


# Line plot
Years=[2010,2022,2012,2013]
sales=[100,120,140,150]
plt.plot(Years,sales, label="sales trends", color="blue", marker="o" )
plt.title("sales over Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.show()