"""
simple linear regression:
we use this model for continuos and infinite values
linear relation between one independent variable and one dependent variable
e.g: y=mx+c
y value depends on x
here y value continuos according with x
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.DataFrame({'Head size':[1,2,3,4,5],
                 'Brain-Weight':[3009,3998,4890,6500,6900]})
print(df)
"""
   Head size  Brain-Weight
0          1          3009
1          2          3998
2          3          4890
3          4          6500
4          5          6900
"""
print("--------------------------")
print(df.describe())
"""
      Head size  Brain-Weight
count   5.000000      5.000000
mean    3.000000   5059.400000
std     1.581139   1644.881698
min     1.000000   3009.000000
25%     2.000000   3998.000000
50%     3.000000   4890.000000
75%     4.000000   6500.000000
max     5.000000   6900.000000
"""
# we can think here as head size increases brain also increases
x=df['Head size'] # independent
y=df['Brain-Weight'] #dependent
plt.plot(x,y)
plt.show()
print("---------ml-------------")
#linear regression
#eq of line y=mx+c
print(type(x)) # it is in series
print(type(df)) # dataframe
print("--------------------------")
xx=[i for i in range(1,10)]
m=0.3
c=0.4
for num in xx:
    y=m*num+c
    print(y)