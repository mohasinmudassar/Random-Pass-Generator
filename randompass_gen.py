 # simple :

"""
import random
import string

def password(length):
    pw=str ()
    characters = "abcdefg"
    for i in range (length):
        pw = pw +random.choice(characters)
    print(pw)


password(4)"""



# using ascii and etc :


import random
import string

def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(6):
        password += random.choice(random_source)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

print("First Random Password is ", get_random_password())
print("Second Random Password is ", get_random_password())