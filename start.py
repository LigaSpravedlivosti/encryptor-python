import os
from Crypto import Random
from Crypto.Cipher import DES
from Crypto.Cipher import AES
import config

def start():
    file = input('Put the file you want to encrypt or decrypt into the folder with the start.py\n'
                 'Name of file(name.extension):')
    if file not in os.listdir(path = os.getcwd()):
        print('>>>>Error. There is not such a file ' + file + '.')
        start()
    else:
        config.file = file
        setoperation()

def setoperation():
    oper = input('To encrypt type "E", to decrypt type "D"\n')
    if oper == 'E' or oper == 'D':
        config.oper = oper
        setalgorithm()
    else:
        print('>>>>Error. There is not such an option.')
        setoperation()

def setalgorithm():
    alg = input('Choose one option\n'
                '-DES(type "DES")\n'
                '-AES(type "AES")\n')
    if alg == 'DES':
        des_encr(config.file) if config.oper == 'E' else des_decr(config.file)
    elif alg == 'AES':
        aes_encr(config.file) if config.oper == 'E' else aes_decr(config.file)
    else:
        print('>>>>Error. There is not such an option.')
        setalgorithm()

def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text

def des_encr(file):
    key = input('Type the secret key (length = 8): ')
    if len(key) == 8:
        key = key.encode()
        with open(file,'rb') as nf:
            des = DES.new(key, DES.MODE_ECB)
            data = nf.read()
            padded_data = pad(data)
            encrypted_data = des.encrypt(padded_data)
            with open('encrypted_' + file,'ab') as encrypted_file:
                encrypted_file.write(encrypted_data)
        print('File was succesfully encrypted.')
        start()
    else:
        print('Length of your secret key should be equal to 8')
        des_encr(file)

def des_decr(file):
    key = input('Type the secret key (length = 8): ')
    if len(key) == 8:
        key = key.encode()
        with open(file,'rb') as nf:
            des = DES.new(key, DES.MODE_ECB)
            data = nf.read()
            padded_data = pad(data)
            decrypted_data = des.decrypt(padded_data)
            with open('decrypted_' + file,'ab') as decrypted_file:
                decrypted_file.write(decrypted_data)
        print('File was succesfully decrypted.')
        start()
    else:
        print('Length of your secret key should be equal to 8')
        des_decr(file)

def aes_encr(file):
    key = input('Type the secret key (length = 16): ')
    if len(key) == 16:
        key = key.encode()
        with open(file,'rb') as nf:
            aes = AES.new(key, AES.MODE_ECB)
            data = nf.read()
            padded_data = pad(data)
            encrypted_data = aes.encrypt(padded_data)
            with open('encrypted_' + file,'ab') as encrypted_file:
                encrypted_file.write(encrypted_data)
        print('File was succesfully encrypted.')
        start()
    else:
        print('Length of your secret key should be equal to 16')
        aes_encr(file)

def aes_decr(file):
    key = input('Type the secret key (length = 16): ')
    if len(key) == 16:
        key = key.encode()
        with open(file,'rb') as nf:
            aes = AES.new(key, AES.MODE_ECB)
            data = nf.read()
            padded_data = pad(data)
            decrypted_data = aes.decrypt(padded_data)
            with open('decrypted_' + file, 'ab') as decrypted_file:
                decrypted_file.write(decrypted_data)
        print('File was succesfully decrypted.')
        start()
    else:
        print('Length of your secret key should be equal to 16')
        aes_encr(file)

start()
    
        
