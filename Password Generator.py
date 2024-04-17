import secrets
import random
import string

def generator(num):
    grp1 = string.ascii_uppercase
    grp2 = string.ascii_lowercase
    grp3 = string.digits
    grp4 = "!#$%&*,<=>?@|~"

    rem_char = [grp1, grp2, grp3, grp4]

    key = secrets.choice(grp1)
    key += secrets.choice(grp2)
    key += secrets.choice(grp3)
    key += secrets.choice(grp4)

    for i in range(num-4):
        key += secrets.choice(rem_char[secrets.randbelow(4)])
        
    return key

def shuffle(chars):
    ls_char = list(chars)
    random.shuffle(ls_char)
    return ''.join(ls_char)

num_chars = int(input("What is the length of password you want (atleast 8 recommended)?\n"))

password = generator(num_chars)

print(f"Your generated password is: {shuffle(password)}")