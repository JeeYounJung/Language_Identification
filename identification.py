import sys
import math
import string


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X=dict.fromkeys(string.ascii_uppercase, 0)
    with open (filename,encoding='utf-8') as f:
        readf = f.read()
        for i in readf:
            if i.upper() in X:
                X[i.upper()] += 1


    return X



# TODO: add your code here for the assignment
# You are free to implement it as you wish!
# Happy Coding!

#Q1
print("Q1")
f = shred("letter.txt")
for i,j in f.items():
    print(i, j)

#Q2
print("Q2")
vector = get_parameter_vectors()
english = f["A"] * math.log(vector[0][0])
spanish = f["A"] * math.log(vector[1][0])
# k, v = list(f.items())[0]
# spanish = v * math.log(vector[1][0])
print(float("%.4f"%english))
print(float("%.4f"%spanish))

#Q3
print("Q3")
eIndex = 0
eValue = 0
sIndex = 0
sValue = 0

for i in f.items():
    numValue = i[1] * math.log(vector[0][eIndex])
    eValue += numValue
    eIndex += 1
fEnglish = eValue + math.log(0.6) #english
print(format(fEnglish, '.4f'))

for j in f.items():
    numValue = j[1] * math.log(vector[1][sIndex])
    sValue += numValue
    sIndex += 1
fSpanish = sValue + math.log(0.4) #spanish
print(format(fSpanish, '.4f'))

#Q4
print("Q4")
pEnglish = 0

if fSpanish - fEnglish >= 100:
    pEnglish = 0
elif fSpanish - fEnglish <= -100:
    pEnglish = 1
else:
    pEnglish = 1/(1 + math.exp(fSpanish - fEnglish))

print(format(pEnglish, '.4f'))