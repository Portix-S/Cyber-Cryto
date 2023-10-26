
p = 17
q = 23
e = 65537

N = p * q


numberToEncrypt = 12

encrypted = pow(numberToEncrypt, e) % N
print(encrypted)