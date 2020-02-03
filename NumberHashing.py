import random
plaintext = input("Data to hash: ")
password = input("Password to hash with: ")
itercount = input("Number of password iterations: ")
plaintextord = 0
passwordSeed = ''
plaintextSeed = ''
key = 0
for i in plaintext:
    plaintextord += ord(i)
for i in password:
    passwordSeed += str(ord(i))
for i in plaintext:
    plaintextSeed += str(ord(i))
for i in range(int(itercount)):
    random.seed(int(plaintextSeed) + i)
    plaintextord += random.randint(1000, 1000000000)
for i in range(int(itercount)):
    random.seed(int(passwordSeed) + i)
    key += random.randint(1000, 1000000000)
print("Your hashed text:")
print(key * plaintextord * plaintextord)
