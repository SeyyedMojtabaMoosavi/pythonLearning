"""in the name of God"""
"""
      یک راهنمایی هستش برای سایر برنامه نویسان که کد های ما رو میخوانندannotation"""

#دقت شود این انونیشن ها در کامپایل نادیده گرفته میشوند
def show(name :str, age:int) ->  str:
    return f' {name} is {age } old'

#ما میتوانیم برای این گار حتی توضیح را داخل گیومه بزاریم
def show2(name :"name", age:"inter your age") ->  "this function return str":
    return f' {name} is {age } old'

a=show2('mojtaba',37)
print(a)



#typing


import typing as tp
#tp.Dict[str,int]
#point= tp.List[str]     you can replec this code
def show3(names: tp.List[str]):
    for name in names:
        print(name)


show3(['amir','nojtaba','aaxa'])

