# Non Feedback Demonstration

#Find New flow velocity in pipe with different diameter
def Bernoulli_Velocity(oldDiameter,oldVelocity,newDiameter):
    #y = V * pow2(D1) / pow2(D2) 
    temp = oldVelocity * pow(oldDiameter,2)
    newVel = temp / pow(newDiameter,2)
    return newVel

