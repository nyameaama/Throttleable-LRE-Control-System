import random

#Test data (Under , Nominal, Over)
#Input
# Range

#Returns
# - Inlet value

#Experimental:
# - Outlet value


def generateTestData(RANGE_LOW,RANGE_HIGH,batch_size):
    testData = UnorderedSequence(RANGE_LOW,RANGE_HIGH,batch_size)
    return testData


def UnorderedSequence(low,high,size):
    #Generated sequence will follow not follow any pattern. Numbers will 
    # be generated at random within a range (ex:5-7). 
    seq = []
    values_generated = 0
    count = 0
    for values_generated in range(0,size):
        #get random int between range
        seq.append(random.randint(low,high))
        values_generated += 1
    
    return seq

#########################################################################
def OrderedSequence(low,high,size):
    #Generated sequence will follow pattern. Numbers will 
    # be generated at random within a range (ex:5-7). Each rand
    # number from RANGE_LOW will be greater than last while <= RANGE_HIGH
    current_num = low
    values_generated = 0
    seq = []
    # Deal with batch size 
    # Get max -- from 1 decimal place (0.1,0.2,0.3......,0.9)
    temp = (high - low) * 10
    if(size > temp):
        v = 0

    #array count
    count = 0
    while  current_num < high and values_generated < size:
        seq[count] = random.randint()
        
#########################################################################
print(UnorderedSequence(20,25,20))
#print(random.randint(20,25))