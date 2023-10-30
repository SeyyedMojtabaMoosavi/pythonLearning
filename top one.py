from collections import Counter as c

lis=[1,1,1,3,34,23,3,54,3,23,234]
print(c(lis))
def show(arr):
    values={}
    result=[]
    top_value=0
    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i]=1
    print(values)
    top_value=max(values.values())
    for i in values:
        if values[i] == top_value:
            result.append(i)

        else:
            continue

    return result


print(show(lis))