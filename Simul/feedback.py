import math

#Feedback Demonstration - PID

error_integral = 0
error_previous = 0

#PID
def PID(current,setpoint):
    kp = 0.5
    ki = 0.2
    kd = 0.1
    dt = 1
    processVar = current
    error = setpoint - processVar
    error_integral += error * dt
    derivative = (error - error_previous) / dt
    error_previous = error
    dv =  kd * derivative
    integral = ki * error_integral
    prop = kp * error
    result = prop + integral + derivative
    return result

#Find New flow velocity in pipe with different diameter
def Bernoulli_Velocity(oldDiameter,oldVelocity,newDiameter):
    #y = V * pow2(D1) / pow2(D2) 
    temp = oldVelocity * pow(oldDiameter,2)
    newVel = temp / pow(newDiameter,2)
    return newVel


