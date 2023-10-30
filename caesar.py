from string import ascii_letters

def incrypt(string,key):
    result=''
    alpha=ascii_letters
    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            new_key=(alpha.index(ch) + key ) %  len(alpha)
            result += alpha[new_key]
    return result
print(incrypt("salam", 3))
def decrypt(string,key):
    k=key * -1
    return (incrypt(string,k))
print(decrypt('vdodp',3))

def brute_force(string):
    key= 1
    result=''
    brute_force_data={}
    alpha = ascii_letters
    while key <= len(alpha):
        result = decrypt(string,key)
        brute_force_data[key] = result
        key += 1
    return brute_force_data

print(brute_force("vdodp"))






