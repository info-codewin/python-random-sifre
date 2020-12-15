#https://discord.gg/cMpeHRYCHN
#Made by WİN CODE
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
combined = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '#', '$', '%', '^',
            '&', '*','/', '-', ':', '_', '`', '~']

minimum = int(input('Şifre uzunluğu giriniz:'))
special_char = input('Özel karaterler olsunmu ?(Evet Veya Hayır):')

if special_char == 'Hayır':
    password = ''
    length = random.randint(minimum, minimum+0)
    for i in range(length):
        data = random.choice(letters)
        password = password + data
    print(password)
elif special_char == 'Evet':
    password = ''
    length = random.randint(minimum, minimum+0)
    for i in range(length):
        data = random.choice(combined)
        password = password + data
    print(password)
