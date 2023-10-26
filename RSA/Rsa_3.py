
p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
numberToEncrypt = 12

N = p * q
totient = (p - 1) * (q - 1)
print("totient of N: ", totient)

privateKey = pow(e, -1, totient) # e^-1 mod totient (modular inverse)
print("private key: ", privateKey)


encrypted = 77578995801157823671636298847186723593814843845525223303932 #pow(numberToEncrypt, e, N)
#print(encrypted)

decrypted = pow(encrypted, privateKey, N) 
print("decrypted: ", decrypted)