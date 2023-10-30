#in the name of God


#meta class
#در اینجا چی اومده و کلاس  ای رو ایجاد کرده و به شکل یک ابجکت برای نیو فرستاده؟؟؟؟
#متا کلاس ها کلاسهایی هستند که به شما اجازه میدهند تا شما رفتار سایر کلاس ها رو تغییر بدهید
class A:
    def __new__(cls, *args, **kwargs):
        return cls


a=A()
print(a)

#type(name, bases, dict, **kwds) -> a new type  شما میتوانید از طریق تایپ یک کلاس  جدید بسازید.
b = type('classname',(),{})    #creat a new class "classname"
print(b)
# help(type)


#کلاس تایپ بالاترین متاکلاس در پایتون میباشد
#----------------------------------------------------crat a metaclass
#ما در اینجا کاری کردیم که با متا کلاسها که فقط یک اینستنس از کلاس ما بتواند ساخته شود

class Singelton(type):
    _instance=None
    def __call__(self,*args,**kwargs):
        if self._instance is None:
            self._instance == super.__call__()
        return self._instance

class db(metaclass=Singelton):
    pass

d1=db()
d2=db()
#میبینیم که ما  فقط یک ادرس را خواهیم داشت
print(id(d1))
print(id(d2))