import pandas as pd
# Series--->one dimentional labeled array capable of holding data of any type
# dataframe--->two dimentional labeled data structure like table 

s=pd.Series([1,2,3], index=["a", "b", "c"])
print(f" \n{s}")

# dataframe
data={"name: ":["usman", "waris","ali"], "ages: ":[22,23,24]}
d_frame=pd.DataFrame(data)
print(f"\n{d_frame}")


# loading data fro csv, excel and other 
'''common data loading method 
        -From CSV
        -From EXCEL
        -From Dictionary
saving data
        -save to excel
        -save to csv
''' 
# read data 
rd_csv=pd.read_csv("mydata.csv" )
rd_excel=pd.read_excel("mydata.xlsx")

# save data 
rd_csv.to_csv("mydata.csv",index=False)
rd_excel.to_excel("mydata.csv",index=False)


# viewing data----->first five rows
rd_csv.head()
rd_csv.tail(3)  #last three rows
rd_csv.info()   #summary of the data frames
rd_csv.describe() #statistical summary of data frame

'''
selecting and indexing 
    -slecting colums
    -filtering rows
    -selecting by position
    -seleting by labels 

'''
df= rd_csv["name", "regno"]  #selecting colums
print(rd_csv[rd_csv["ages"]>20])  #filtering rows
print(rd_csv.iloc[0]) #first row 
print(rd_csv.iloc[:,0]) #first colums iloc index based and loc lable base 
print(rd_csv.loc[:,"Name"])




