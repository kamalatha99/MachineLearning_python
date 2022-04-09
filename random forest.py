"""
random forest:
it performs both classification and regression
it is ued for large datasets
it takes less time for prediction
there is no problem of overfitting
under fitting: unable to predict output
over fitting:
------voting classifier
 is a machine learning model
 --------boodting classifier
  strong classifier
over fitting
->e.g: robo
after lots of training
failed in testing
"""
import pandas as pd
from sklearn.datasets import load_digits
digit=load_digits()
k=digit.keys()
print(k)
data=pd.DataFrame(digit.data)
print(data)
data['Digit']=digit.target
print(digit.images)