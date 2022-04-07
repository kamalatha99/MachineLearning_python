import pandas as pd
#converting tuple
t=(2,4,7,'hok','hill')
print(t,type(t))
con_t=pd.Series(t)
print(con_t,type(con_t))
print("-----------------------")
#converting string to list and then series
str="hello kammi practise well"
print(str)
l=str.split()
print(l,type(l))
con_l=pd.Series(l)
print(con_l,type(con_l))
print("------------------------")
#converting dictionary
dic={
    'f':1,'s':2,'third':3
}
print(dic,type(dic))
con_d=pd.Series(dic)
print(con_d,type(con_d))

