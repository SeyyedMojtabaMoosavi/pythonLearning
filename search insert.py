def search_insert(arr,val):
    low=0
    high=len(arr) - 1
    mid = high // 2
    while low <= high:
        if val > arr[mid]:
            mid +=1
            low= mid
        else:
            mid -=1
            high=mid

    return low
print(search_insert([1,4,5,6,8],10))



"""
def is_somorphic(s,t):
    if len(s) != len(t):
        return False
    dict={}
    set_value=set()
    for i in range(len(s)):
        if s[i] not in dict:
           if t[i] in set_value:
             return False
           dict[s[i]]=t[i]
           set_value.add(t[i])
        else:
            if dict[s[i]] != t[i]:
                return False
    return True
print ( is_somorphic('bew','foo'))
"""

