import pandas as pd
s=pd.Series({10:'hello',20:'hai',30:'bye',40:0})
print(s)
print(dir(s))
print("----------------------------")
#sort
nums=[2,4,5,3,6]
con_l=pd.Series(nums)
print(con_l)
print(con_l.sort_values())
#print(dir(con_l))
print("-----------------------------")
#drop
help(con_l.drop)
print(con_l.drop(3))
print("------------------------------")
r=range(10,20,5)
con_r=pd.Series(r)
print(con_r)
print("-------------------------------")
import numpy as np
r1=np.random.randint(10,20,5)
con_r1=pd.Series(r1,index=['one','two','three','four','five'])
print(con_r1)
print("---------------------------------")
#indexing
s.index=[i for i in range(60,64)]
print("index",s)
print("-----------------------------------")
print("append(),add(),all(),apply(),any()")
app=s.append(con_r1)
print(app)
print("if every value is true",s.all())
print("if any element is true",s.any())
