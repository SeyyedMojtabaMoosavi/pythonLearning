#in the name of God

""" __call__ method

متد کال به ما اجازه میدهد  که نمونه هایی که از کلاس ها ایجاد میکنیم رو بتونیم مثل یک فانکشن صدا بزنیم

این داندر زمانی فعال میشود که ما یک اینستنس رو به شکل فانکشن صدا بزنیم یعنی در مقابل یک اینستنس ما پرانتز بزاریم
"""


class A:
    def __call__(self, name,*args, **kwargs):
        print(name,"call method......")



a=A()

a('amir')