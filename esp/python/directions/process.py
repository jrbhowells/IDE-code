'''
Program to read directions.txt coordinate array and fold onto one line

J Howells / IDE Group 1
Dyson School of Design Engineering
26/5/2022
'''

with open("directions.txt", 'r') as file:
    data = file.read()
    file.close()

data = data.replace("\n", "")
data = data.replace(" ", "")
print(data)

with open("directions.txt", 'w') as file:
    file.write(data)
    file.close()