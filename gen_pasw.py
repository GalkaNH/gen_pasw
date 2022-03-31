import random
import string

all = string.ascii_letters + string.digits + string.punctuation

password_len = int(input('Długość hasla:  '))
password = "".join(random.sample(all, password_len))
print(password)
