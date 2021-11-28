import string
import random


replacable = list(chr(i) for i in range(128)) 
replacable.append("split")

valid_seed_characters = list(string.ascii_letters + string.digits)


def randstring():
    s = ""
    randint = random.randint(10, 20)
    for i in range(randint):
        s += random.choice(valid_seed_characters)

    return s

def createkey():
    key = {}

    for i in replacable:
        key[i] = randstring()

    seeds = []
    matches = 0
    duplicates = []
    for k in key:
        if key[k] in seeds:
            matches += 1
            duplicates.append(key[k])
        
        seeds.append(key[k])

    if matches > 0:
        createkey()

    return key

