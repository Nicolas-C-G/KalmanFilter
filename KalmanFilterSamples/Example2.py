import numpy as np
import matplotlib.pyplot as plt

#Example2 - Tracking the constant velocity aircraft in one dimention
#
# The Update State Equation for position
#
#  x(n,n) = x(n,n-1) + alpha * (z(n) - x(n,n-1))
#
# The Update State Equation for velocity
#
#   d(x(n,n))/dx = d(x(n,n-1))/dx + beta * ((z(n) - x(n,n-1))/deltaT)

#Init variables
alpha  = 0.2
beta   = 0.1
deltaT = 5 #seconds
radarMeasurement = [30110, 30265, 30740, 30750, 31135, 31015, 31180, 31610, 31960, 31865]


position           = [] #m/s
velocity           = [] #m
predictionPosition = []
predictionVelocity = []
SUEposition        = []
SUEvelocity        = []


position.append(30000)
velocity.append(40)

for i in range(len(radarMeasurement)):
    if i < 1:
        # Prediction first iteration
        predictionPosition.append(position[i] + (deltaT*(velocity[i])))
        predictionVelocity.append(velocity[i])

    # Calculating the current estimate using the State Update Equation
    SUEposition.append(predictionPosition[i] + alpha * (radarMeasurement[i] - predictionPosition[i]))
    SUEvelocity.append(predictionVelocity[i] + beta  * ((radarMeasurement[i] - predictionPosition[i]) / deltaT))

    # Calculating the next state estimate using the State Extrapolation Equations
    position.append(SUEposition[i] + (deltaT * (SUEvelocity[i])))
    velocity.append(SUEvelocity[i])

    predictionPosition.append(position[i+1])
    predictionVelocity.append(velocity[i+1])


data = np.zeros((len(position)-1,2))
time = 5
for x in range(len(position)-1):
    data[x,1] = time
    data[x,0] = position[x+1]
    time += 5

print(data) #Print the values of Estimations (m) v/s time (s)