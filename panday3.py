import pandas as pd

print("pandas means panelData(roes,col)")
print("used for data analysis,manuplations and cleaning ")
print("2data structures we useseries and  datafarame")
print("-------------------------------------------------------")
print("to check version")
print(pd.__version__)
print("--------------------------------------------------------")
print("to check available methods for panadas")
print(dir(pd))
print("---------------------------------------------------------")
print("series:sequence data")
str="hello kamalatha"
print(str,type(str))#string type
print(type(pd.Series(str)))
print(pd.Series(str)) #object type
print("----------------------------------------------------------")
table={'int':[9,87,90,1004,34],'float':[9.6,45.4,34.76,45.3,5.6],'str':['abc','def','ghi','jkl','mno']}
frame=pd.DataFrame(table)
print(frame)
print("----------------------------------------------------------------")
d1={
    'color':['red','green','black'],
    'laptop':['hp','dell','asus']
}
df1=pd.DataFrame(d1)
d2={
    'color':['orange','blue','purple'],
    'laptop':['lenovo','apple','acer']
}
df2=pd.DataFrame(d2)
print(df1)
print(df2)
