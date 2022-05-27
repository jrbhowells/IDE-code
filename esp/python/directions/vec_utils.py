'''
Utilities to process vectors

J Howells / IDE Group 1
Dyson School of Design Engineering
26/5/2022
'''

import math

# Turn start and end coordinate arrays into a vector
def createVector(start, end):
    return [end[0]-start[0], end[1]-start[1]]

# Calculate magnitude of vector
def vectorMag(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2)

'''
Incomplete
# Calculate distance from vector to point
def distanceTo(data, point):
    cl_ptr = findClosest(point, data)

    possible1 = [data[cl_ptr], data[cl_ptr+1]]
    possible2 = [data[cl_ptr-1], data[cl_ptr]]
'''

# Calculate angle between vectors
def angleBetween(vec1, vec2):
    numerator = vec1[0] * vec2[0] + vec1[1] * vec2[1]
    denominator = vectorMag(vec1) * vectorMag(vec2)
    return math.degrees(math.acos(numerator / denominator))

# Find closest coordinate in a dataset. Return it's position in an array.
# Converts dataset to list of distances then finds minimum
def findClosest(location, dataset):
    for i in range(len(dataset)):
        dataset[i] = [dataset[i][0] - location[0], dataset[i][1] - location[1]]
        dataset[i] = vectorMag(dataset[i])
    
    return dataset.index(min(dataset))