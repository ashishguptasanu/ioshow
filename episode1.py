import numpy as np 
import matplotlib.pyplot as plt 

#values in celcius
cvalues = [20.1, 30.1, 37.81, 32.5, 56.7]

C = np.array(cvalues)
print("Temperature(c): ",C)

#converting celcius values to fahrenheit
C = C * 9/5 + 32
print("Temperature(f): ",C)

#plotting the values
plt.plot(C)

#showing the plot
plt.show()
