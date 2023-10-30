
def is_isomophic(s, t):
    if len(s) != len(t):
        return False
    dict={}
    set_value=set()
    for i in range(len(s)):
        if t[i] in set_value:
            return False
        if s[i] not in dict.keys():

            dict[s[i]] = t[i]
            set_value.add(t[i])
        else:
           if dict[s[i]] != t[i]:
               return False

    return True
print(is_isomophic('fow','fee'))
