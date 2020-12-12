from Testdata import generateTestData

# Non Feedback Demonstration

def pushInletDummyData():
    flowVelocityLOW = 0
    flowVelocityHIGH = 0
    batch_size = 10
    return generateTestData(flowVelocityLOW,flowVelocityHIGH,batch_size)

#Find New flow velocity in pipe with different diameter
def Bernoulli_Velocity(oldDiameter,oldVelocity,newDiameter):
    #y = V * pow2(D1) / pow2(D2) 
    temp = oldVelocity * pow(oldDiameter,2)
    newVel = temp / pow(newDiameter,2)
    return newVel

