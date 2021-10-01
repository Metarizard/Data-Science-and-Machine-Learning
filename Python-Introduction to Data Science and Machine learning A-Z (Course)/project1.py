import numpy as np
import pandas as pd
import scipy as sp
from scipy import integrate, cluster, fftpack, special

# Numpy code

var1 = np.array([(1,2,3),(2,4,6)])
print(np.std(var1.sum()))


# Pandas code

employee = {'number':[1,2,3,4,5], 'name':["abby","john","lina","marc","bob"], 'salary':[15,25,32,27,40]} # Dictionary like

table = pd.DataFrame(employee)
print(table.tail(3))

# Scipy code

angle = special.sindg(5)
print(angle)

integrand = lambda y,x: x * y**4

result = integrate.dblquad(integrand, 0, 6, lambda x:0, lambda x:1)

print(result)