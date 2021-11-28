
# November 24th 2021
# Cryptor.py is part of an encryption program I am making.
# Author; Grubbsy
# Created in Chicago Illinois


import json
from os import defpath
from dataloader import save_json, ROOT_DIR
import easygui
from encryptor import encrpyt
from decryptor import decrypt
from keygen import createkey
import wx


# 
# Funcs
#


# From Stack overflow.
# https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python/9319832#9319832
def get_path():
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path

def usekey(ask=True):
    u = "yes"
    if ask:
        u = input("Load key (yes/no): ")

    if u.lower() == "y" or u.lower() == "yes":
        keypath = get_path()
        with open(keypath, 'r') as kf:
            k = kf.read()
            newkey = json.loads(k)

        return newkey
    else:
        return createkey()



# OPENING THE FIRST FILE
file = get_path()
data = ""


try:
    with open(file, 'r') as f:
        data = f.read()
except Exception as e:
    print(e)
    print("Couldn't Open The File.")

# Getting Input
inp = input("Select a mode: \n1. Encrypt \n2. Decrypt\nMode:   ")

# We encrypting here.
if str(inp) == "1":
    key = usekey()
    newdat = encrpyt(key, data)

    ext = input("What file extension to give (Don't add a . ):     ")
    filename = input("Filename: ")

    with open(f"{ROOT_DIR}/outputs/{filename}.{ext}", 'x') as newfile:
        newfile.write(newdat)
    with open(f"{ROOT_DIR}/outputs/{filename}.key",  'x') as newfile:
        newfile.write(json.dumps(key))

    print("Encrypting Complete.")
#===

# Decrypting here.
if str(inp) == "2":
    key = usekey(False)
    newdat = decrypt(key, data)
    print("Decryted Data\n==========")
    print(newdat)
    print("==========")

    save = input("Save File?  ")
    if save.lower() == "yes" or save.lower() == "y":
        name = input("Filename: ")
        with open(f"{ROOT_DIR}/outputs/{name}_decrypted.txt", 'x') as newfile:
            newfile.write(newdat)
        
        print(f"Saved at {ROOT_DIR}/outputs/{name}_decrypted.txt")
    else:
        print("File Not Saved.")

# with open(f"{ROOT_DIR}/output.txt", 'x') as newfile:
#     newfile.write(output)

# This is a test file to encrypt
# I like to program a lot and I'm just testing as many characters as I can.

# A Good password would be one like: 
# P455W0RD!@#$%^ 

# Because it has a lot of numbers and symbols. 
# IT IS MISSING LOWERCASE CHARACTERS THOUGH>>>>>> 
