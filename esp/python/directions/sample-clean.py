'''
Program to clean sample GPX data onto array.
Requires all tags other than those around the coords themselves to be stripped manually.

J Howells / IDE Group 1
Dyson School of Design Engineering
26/5/2022
'''

with open("sample-cycle.txt", 'r') as file:
    data = file.readlines()
    file.close()

for i in range(len(data)):
    data[i] = data[i].replace('<trkpt lat="',"[")
    data[i] = data[i].replace('" lon="', ',')
    data[i] = data[i].replace('"/>', ']')
    data[i] = data[i].replace(' ', '')

with open("sample-cycle.txt", 'w') as file:
    file.write(''.join(data))
    file.close()