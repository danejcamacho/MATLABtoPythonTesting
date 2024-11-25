import re

pyfile = open('python_output.txt', 'r')
pylines = pyfile.readlines()

matfile = open('matlab_output.txt', 'r')
matlines = matfile.readlines()


#each index is one answer
#each answer is a list of numbers (float or int)
pylist = []
matlist = []



for i in range(len(pylines)):
    # #take each line and turn it into a list of numbers
    
    #use regex to remove special characters from pylines and matlines[i]
    pylines[i] = re.sub(r'[^\d.-]+', ' ', pylines[i])

    
    #split the string into a list of numbers
    pylines[i] = pylines[i].split()
    matlines[i] = matlines[i].split()
    
    pylist.append(pylines[i])
    matlist.append(matlines[i])

print(pylist)
print(matlist)

#convert the strings to floats or ints
for i in range(len(pylist)):
    for j in range(len(pylist[i])):
    
        if '.' in pylist[i][j]:
            pylist[i][j] = float(pylist[i][j])
            matlist[i][j] = float(matlist[i][j])
        else:
            pylist[i][j] = int(pylist[i][j])
            matlist[i][j] = int(matlist[i][j]) 

    
    
for i in range(len(pylist)):
    #compare the two lists
    #if the lists are the same, print "Valid"
    #if the lists are different, print "Invalid"
    if pylist[i] == matlist[i]:
        print("Valid")
    else:
        print("Invalid")



    