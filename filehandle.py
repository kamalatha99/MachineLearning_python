with open("check") as file:
    print(file.read())
"""
hello my name is kamalatha poluparthi welcome to
machine learning using python workshop
"""
with open("marks.csv") as f:
    print(f.read())
"""
Name,wt,iot,Mefa,Ds
lala,45,34,53,43
jala,65,56,54,34
rana,65,45,35,35
gama,56,76,35,45
sreenu,67,45,67,32
lalli,45,45,35,33
scott,45,23,22,12
"""
import pandas as pd
df=pd.read_csv("marks.csv")
print(df)
"""
     Name  wt  iot  Mefa  Ds
0    lala  45   34    53  43
1    jala  65   56    54  34
2    rana  65   45    35  35
3    gama  56   76    35  45
4  sreenu  67   45    67  32
5   lalli  45   45    35  33
6   scott  45   23    22  12
"""
print(df.head()) #gets first 5 rows
print("------------------")
print(df.tail()) #gets last five rows
print("--------------------------")
print(df.head(2))
print("--------------------------")
print(df.tail(2))
print("---------------------------")
print(df.sample())#gets one random sample
print(df.sample(3))#gets 3 samples
print("------------------------------")
#describe
print(df.describe())
"""
         wt        iot       Mefa         Ds
count   7.000000   7.000000   7.000000   7.000000
mean   55.428571  46.285714  43.000000  33.428571
std    10.357882  16.710419  15.438048  10.721585
min    45.000000  23.000000  22.000000  12.000000
25%    45.000000  39.500000  35.000000  32.500000
50%    56.000000  45.000000  35.000000  34.000000
75%    65.000000  50.500000  53.500000  39.000000
max    67.000000  76.000000  67.000000  45.000000
"""
print("-----------------------------")
print(df.info())
print("------------------------------")
# to check null values
print(df.isnull())
"""
    Name     wt    iot   Mefa     Ds
0  False  False  False  False  False
1  False  False  False  False  False
2  False  False  False  False  False
3  False  False  False  False  False
4  False  False  False  False  False
5  False  False  False  False  False
6  False  False  False  False  False"""

print("------------------------------")
# adding a column total of subjects
print(df.wt)
df['total']=df['wt']+df['iot']+df['Mefa']+df['Ds']
print(df)
print("----------------------------------")
df['sum']=df.iloc[:,1:].sum(axis=1)
df.index[1,2,3,4,5,6,7]
print(df)
print("----------------------------------")