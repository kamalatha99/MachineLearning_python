"""
# create the following dataframe
Int     Float    Str
9        9.6      str1
87       45.4     str2
90      34.76     str3
1004    45.3      str4
34       5.6      str5
"""
import pandas as pd
dic={
    'Int':[9,81,24,3101,41],
    'Float':[2.4,3.3,4.8,2.0,5.8],
    'str':['s1','s2','s3','s4','s5']
}
s=pd.Series(dic)
print(s)
"""
Int          [9, 81, 24, 3101, 41]
Float    [2.4, 3.3, 4.8, 2.0, 5.8]
str           [s1, s2, s3, s4, s5]
dtype: object
"""
df=pd.DataFrame(dic,index=[1,2,3,4,5])
print(df)
"""
    Int  Float str
1     9    2.4  s1
2    81    3.3  s2
3    24    4.8  s3
4  3101    2.0  s4
5    41    5.8  s5
"""
print(df.Float)# retrive  single column
"""
1    2.4
2    3.3
3    4.8
4    2.0
5    5.8
"""
print(df[['Int','Float']])# retrive multiple columns
"""
    Int  Float
1     9    2.4
2    81    3.3
3    24    4.8
4  3101    2.0
5    41    5.8
"""
df['bool']='yes'#added a column
print(df)
