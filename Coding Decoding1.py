# Program to take string in raw or coded form as input and provide coded or raw form.

#FUNCTIONS
#start
def codeit(a):
    '''Function to take string in raw form as input and provide in coded form'''
    print(f"You entered {a}.\nCode = ", end="")

    for i in range(len(a)-1, -1, -1):#iterating the loop in reverse form
        print(a[i], end="")
#end

#start
def decodeit(a):
    '''Function to take string in coded form as input and provide in raw form'''
    print(f"You entered the code {a}.\nDecoded Material = ", end="")

    for i in range(len(a)-1, -1, -1):#iterating the loop in reverse form
        print(a[i], end="")
#end


#PROGRAM
# Program starts here
print("\n\n")
inp = int(input("Do you want to code or decode.\nPress 1 for coding.\nPress 2 for decoding\n"))
txt  = input("Enter your text:\n\n")

# Docstrings
# print(codeit.__doc__)
# print(decodeit.__doc__)

# Conditional statement to direct to code or decode functn
if(inp == 1):
    codeit(txt)
elif(inp == 2):
    decodeit(txt)
print("\n\n")