
lis=[i for i in range(0, 10) ]




def limit(arr,min=None,max=None):
    min_chek=lambda val:True if min is None else val >= min
    max_chek=lambda  val:True if max is None else val< max
    return [val for val in arr if min_chek(val) and max_chek(val)]


print(limit(lis,3,20))

