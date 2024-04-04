# Program to take string in raw or coded form as input and provide coded or raw form.
# Author: Lucifer BloodFallen

#IMPORTS
import random
import string

#FUNCTIONS
# start
def codeit(a):
    '''Function to take string in raw form as input and provide in coded form'''
    letters_collectn = string.ascii_letters #creating a string of all the uppercase and lowercse characters
    rand_lett = ''.join(random.choice(letters_collectn) for i in range(3)) #choosing 3 random letters from letters_collectn

    print(f"You entered {a}.\nCoded form = ", end="")

    print(rand_lett, end="")#printing 3 random letters
    for i in range(len(a)-1, 0, -1):#iterating the loop from second character to last character in reverse form
        rand_char = ''.join(random.choice(letters_collectn) for i in range(1))#choosing a random letter from letters_collectn
        print(a[i], rand_char, sep="", end="")#printing the single character from main string followed by a random letter 

    print(a[0])#printing the 1st character from main string
# end

def decodeit(a):
    '''Function to take string in coded form as input and provide in raw form'''
# start
    print(f"You entered the code {a}.\nRaw form = ", end="")
    print(a[len(a)-1], end="")#printing the last letter

    for i in range(len(a)-3, 2, -2):#iterating the loop from fourth character in reverse form by skiping one letter
        print(a[i], end="")
# end

#PROGRAM
# Program starts here
print("\n\n")
inp = int(input("Do you want to code or decode.\nPress 1 for coding.\nPress 2 for decoding\n"))
txt  = input("Enter your text:\n")
print("\n")

# Docstrings
# print(codeit.__doc__)
# print(decodeit.__doc__)

# Conditional statement to direct to code or decode functn
if(inp == 1):
    codeit(txt)
elif(inp == 2):
    decodeit(txt)
print("\n\n")