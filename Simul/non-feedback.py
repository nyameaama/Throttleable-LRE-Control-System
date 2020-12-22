from Testdata import generateTestData

# Non Feedback Demonstration

flowRanges = [0,0]
actuatorRanges = [0,1]

def main():
    #test data
    testData = pushInletDummyData(5,20)
    actuatorOutputdata = []
    for i in testData:
        valTemp = computeActuatorValue(i,flowRanges[0],flowRanges[1])
        actuatorOutputdata.append(valTemp)
    #Graph

#Generate data sequence
def pushInletDummyData(low,high):
    flowVelocityLOW = low
    flowVelocityHIGH = high
    batch_size = 10
    return generateTestData(flowVelocityLOW,flowVelocityHIGH,batch_size)


#Function to scale reading between actuator range (0,180)
def computeActuatorValue(x,LB,UB):
    #R = (V - M1) * R2 / R1 + M2
    temp1 = 0
    translated_reading = 0
    R2 = (actuatorRanges[1] - actuatorRanges[0])
    R1 = UB - LB
    temp1 = (x - (LB))
    translated_reading = temp1 * (R2 / R1) + actuatorRanges[0]
    return translated_reading

#Find New flow velocity in pipe with different diameter
def Bernoulli_Velocity(oldDiameter,oldVelocity,newDiameter):
    #y = V * pow2(D1) / pow2(D2) 
    temp = oldVelocity * pow(oldDiameter,2)
    newVel = temp / pow(newDiameter,2)
    return newVel

#####
main()
#####