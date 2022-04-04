import random

import numpy as np
"""
random() is a sub module of numpy
used to generate random numbers
---random.rand()
---random.random()
---random.randint()
---random.randn()
"""
r1=np.random.rand(2,2)
print(r1)
print("rand genrates samples")
print("-----------------------------------------")
r2=np.random.random((2,2))
print(r2)
print("random will arrange samples 2 row,2 col with in range 0 to 1 only")
print("-----------------------------------------")
r3=np.random.randint(1,10)
print(r3)
print("generates random integer")
print("-----------------------------------------")
r4=np.random.randn(6,4)
print(r4)
print("it also generates negative values")
print("-----------------------------------------")