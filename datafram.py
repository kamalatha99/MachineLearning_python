"""
dataframe means in the table format of rows and columns
excell sheet type
"""
import pandas as pd
dic={
    571:'dev',581:'swe',588:'jyo'
}
dic_c=pd.DataFrame(dic,index=[1,2,3])
print(dic_c)
"""
output
   571  581  588
1  dev  swe  jyo
2  dev  swe  jyo
3  dev  swe  jyo
"""
drinks={
    'juice':['orange','grapes','banana','mango','sapota'],
    'price':[60,50,40,55,60]
}
print(drinks)
drinks_c=pd.DataFrame(drinks)
print(drinks_c)
"""
    juice  price
0  orange     60
1  grapes     50
2  banana     40
3   mango     55
4  sapota     60
"""
print(drinks_c.columns)#Index(['juice', 'price'], dtype='object')
print(drinks_c.size)#10
i=drinks_c.index=[1,2,3,4,5]
print(drinks_c)
"""
    juice  price
1  orange     60
2  grapes     50
3  banana     40
4   mango     55
5  sapota     60
"""