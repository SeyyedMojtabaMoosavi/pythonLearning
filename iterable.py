#in the name of God

[print(i) for i in range(5)]    #تعداد قابل پیمایش نیستند و برای این موضوع از تابع رنج استفاده میکنیم

"""کلاس هایی که ایجاد میکنید به صورت پیشفرض iterable نیستند. 
برای تبدیل یک آبجکت به iterable باید 
داخل کلاس آن از تابع __iter__ استفاده کنید."""

"""class Friend:
    def __init__(self):
        self.names=['mojtaba','aazam','mohammad hosseyn','zeynab']

fr=Friend()


for i in fr:
    print(i)"""
"""کلاس هایی که ایجاد میکنید به صورت پیشفرض iterable نیستند.
 برای تبدیل یک آبجکت به iterable باید
 داخل کلاس آن از تابع __iter__ استفاده کنید."""
"""هرگاه ما از عبارت return  استفاده کنیم دیگر بعد ان کد ها در ان تایع خوانده نمیشوند

در شرایطی که میخواهیم چند موضوع را بازگشت بدهیم از عبارت yield استفاده میکنیم"""

"""آبجکت های iterator پایتون دقیقا مشابه آبجکت های iterable هستند
 با این تفاوت که به جای اینکه تمام آیتم‌ها را یکجا برگشت دهند، 
 آیتم‌های خود را استریم کرده و تکه تکه برگشت میدهند.
 برای استفاده از آبجکت های iterator دیگر نمیتوان آنها را در حلقه for استفاده کرد 
 بلکه باید با تابع next آنها را صدا زد.

 

برای تبدیل کلاس Friend به یک آبجکت iterator باید به آن تابع __next__ را اضافه کنیم 
که مشخص میکند در زمان فراخوانی با تابع next چه اتفاقی باید بیفتد"""
class Friend:
    def __init__(self):
        self.names=['mojtaba','aazam','mohammad hosseyn','zeynab']

    def __iter__(self):
      #  return iter(self.names)
      #  return self.names.__iter__()
        for name in self.names:
            yield name

    def __next__(self):
        copy_names = self.names
        for name in copy_names:
            return name
        else:
            raise StopIteration
fr=Friend()

print(next(fr))
print(next(fr))
print(next(fr))
print(next(fr))
print(next(fr))
"""for i in fr:
    print(i)"""