import encrypt_decrypt as ed
import os
import time
clear = lambda: os.system('cls')

clear()
print("mellow out")
print("--------------------")
print("**PLEASE PROCEED WITH CAUTION THIS IS A POC**")
print("--------------------")
time.sleep(0)

while True:
    time.sleep(0)
    clear()
    print("Please select an option: ")
    print('''
    --------------------
    1. Generate a new encryption key
    2. Encrypt a given file
    3. Decrypt a given file
    --------------------
    ''')

    x = int(input(""))
    
    if x == 1:
        ed.create_key()

    elif x == 2:
        x = input("Please input a file name to encrypt: ") 
        ed.encrypt(x, ed.load_key())
    
    elif x == 3:
        x = input("Please input a file name to decrypt: ")
        ed.decrypt(x, ed.load_key())
    
    else:
        quit()
