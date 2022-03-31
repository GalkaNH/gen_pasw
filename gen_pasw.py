import random

low = 'qwertyuiopasdfghjklzxcvbnm'
big = 'QWERTYUIOPASDFGHJKLZXCVBNM'
num = '1234567890'
spec = '!@#$%^&amp;*()'

all = low + big + num + spec
password_len = int(input('Długość hasla:  '))
password = "".join(random.sample(all, password_len))
print(password)
