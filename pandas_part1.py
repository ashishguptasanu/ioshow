import pandas as pd 
import numpy as np 

#X = np.array([11, 28, 72, 57, 68])
#S = pd.Series([11, 28, 72, 57, 68])
fruits = ['apples', 'oranges', 'cherries', 'pears']
quantities = [20, 33, 43, 12]
quantities2 = [10, 20, 32, 54]

S = pd.Series(quantities, index=fruits)
S2 = pd.Series(quantities2, index=fruits)
#print(X)
#print(S.index)
#print(S + S2)
#print("Total Quantities: ", sum(S))
print(S['apples'])