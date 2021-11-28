def decrypt(key, data):
    
    # Switching data 
    # So that the 
    # seed points to the letter
    rkey = {}
    for l in key:
        rkey[key[l]] = l
    #

    l = data.split(key['split'])
    s = ""
    
    for item in l:
        if item in rkey:
            s += rkey[item]

    return s
