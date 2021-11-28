def encrpyt(key, data):
    cdat = ""
    for char in data:
        if str(char) in key:
            cdat += (key['split'] + key[str(char)] )
    
    return cdat
