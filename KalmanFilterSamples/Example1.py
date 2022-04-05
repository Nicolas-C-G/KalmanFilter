import numpy as np
import matplotlib.pyplot as plt

#Gold bars example from kalmanfilter.net

#State Update Equation

#   Estimate of     Predicted value                  (                 Predicted     )
#   the current  =  of the current    +  Factor   X  ( Measurement  -  value of the  )
#   state           state                            (                 Current state )

#measurements
GoldBars = np.array([1030, 989, 1017, 1009, 1013, 979, 1008, 1042, 1012, 1011])

DataLenght = GoldBars.size

#initialization
iteration    = 1
x            = np.zeros((DataLenght,2))
z            = np.zeros(DataLenght)
outputs      = np.zeros(DataLenght + 1)
Measurements = np.zeros(DataLenght + 1)
Xaxi         = np.zeros(DataLenght)
x[0][0] = 1000

for i in range(DataLenght):
    Measurements[i+1] = GoldBars[i]
    x[i][1]           = x[i][0]

    #step1
    z[i] = GoldBars[i]

    #step2
    alpha      = 1/iteration #Calculating the gain
    outputs[i+1] = (x[i][1] + alpha*(z[i]-x[i][1]))
    if i < DataLenght-1:
        x[i+1][0]  = outputs[i+1]

    iteration += 1

plt.plot(outputs,'b', Measurements, 'g')
plt.axis([1, 10, np.amin(GoldBars), np.amax(GoldBars)])
plt.title('Measurements v/s Filtered data')
plt.ylabel('Weight (g)')
plt.xlabel('Iterations')
plt.show()