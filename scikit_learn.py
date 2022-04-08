"""
==>>importing a dataset
==>>building a model
==>>used for preprocessing dataset
==>>in preprocessing we need to split the data into training and testing dataset
we give 80% data for training
and 20% for testing
==>>evaluation metrics
"""
import sklearn as skn
print(skn.__version__)
#print(dir(skn))
from sklearn.datasets import load_iris
iris=load_iris()
print(iris)
print("----------------------------")
"""
analyse the data
"""
print(iris.DESCR)# columns
"""

    :Summary Statistics:

    ============== ==== ==== ======= ===== ====================
                    Min  Max   Mean    SD   Class Correlation
    ============== ==== ==== ======= ===== ====================
    sepal length:   4.3  7.9   5.84   0.83    0.7826
    sepal width:    2.0  4.4   3.05   0.43   -0.4194
    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
    petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)
    ============== ==== ==== ======= ===== ====================
"""