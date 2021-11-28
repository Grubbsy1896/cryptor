# cryptor
An Encryptor/Decryptor

(THIS PROGRAM CAN RUN INTO ERRORS THAT WILL WARRANT RERUNNING THE SCRIPT)
This encryptor/decryptor is not perfect by any means, however it is an afternoon project I made. 

### To Run/Use Crpytor
First you need to pip install the following packages

- wxPython

Then, run cryptor.py 

It'll prompt you to open a file, any type, just make sure it's plain text if you're going to encrypt it, or an already encrypted file using this program. Then, after such the program will prompt you if you are 1. Encrypting, or 2. Decrypting. 

Selecting 1 will encrypt the file, however it'll first ask if you want to load an already existing key. If yes, please select a file of a key that was already generated using this program, or make sure it's formatted as a json, and it has all the proper key pairs. It'll then create the file and ask you to name it as it will then save. 

Selecting 2 will decrypt a file, and ask for a key to decrpyt on. It will decrypt correctly with no loss if the key was produced by the program originally. (As the keys generate so that there is little to no overlap, or at least the odds of it happening are very slim. After that, it'll show the decrypted output, and then ask if you want to save it. (If yes, it'll ask you to name the file)
