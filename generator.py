#in the name of God
"""توابع ژنراتور درست مانند توابع معمولی به نظر می رسند و عمل می کنند، اما با یک مشخصه تعیین کننده.
 توابع ژنراتور به جای return از کلمه کلیدی yield پایتون استفاده می کنند.
تابع generator را که قبلا نوشتید به یاد بیاورید:

def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1



این به نظر یک تعریف تابع معمولی است، به جز عبارت yield پایتون و کدی که به دنبال آن است.
yield نشان می دهد که یک مقدار به تماس گیرنده ارسال می شود، اما بر خلاف return، بعد از آن از تابع خارج نمی شوید.
در عوض،
 وضعیت(state) تابع به خاطر سپرده می شود. به این ترتیب، زمانی که next() بر روی یک generator فراخوانی می شود
 (به طور صریح یا ضمنی در یک حلقه for)، متغیر شماره قبلی افزایش یافته و سپس دوباره به دست می آید.
 از آنجایی که توابع generator شبیه توابع دیگر هستند و بسیار شبیه به آنها عمل می کنند،
می توانید فرض کنید که عبارات generator بسیار شبیه سایر comprehensionهای موجود در پایتون هستند."""


def num_last():
    num=0
    while True:
        yield num
        num +=1

fr=num_last()       #تماس گرفتن با یک تابع
print(next(fr))
print(next(fr))
print(next(fr))


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return num
    else:
        return False

"""  ساخت عبارات ژنراتور پایتون(Generator Expressions)

مانند list comprehensionها، عبارات genereator به شما اجازه می دهد تا به سرعت یک شی genereator را تنها در چند خط کد ایجاد کنید. 
آنها همچنین در موارد مشابهی که از list comprehensionها استفاده می شود، با یک مزیت اضافی مفید هستند: 
می توانید آنها را بدون ساختن و نگه داشتن کل شی در حافظه قبل از تکرار ایجاد کنید. به عبارت دیگر،
 هنگام استفاده از عبارات genereator، هیچ جریمه حافظه ای نخواهید داشت. 
این مثال از مربع کردن برخی اعداد را در نظر بگیرید:"""
list_com=[num**2 for num in range(1000)]
list_gen=(num**2 for num in range(1000))


print(list_com)
print(list_gen)
""" ژنراتورها یک راه عالی برای بهینه سازی حافظه هستند.
 در حالی که یک ژنراتور دنباله نامتناهی یک مثال افراطی از این بهینه‌سازی است، 
بیایید نمونه‌های مربع‌سازی اعدادی را که به‌تازگی دیده‌اید تقویت کنیم و اندازه اشیاء حاصل را بررسی کنیم.
 می توانید این کار را با یک فراخوانی به sys.getsizeof() انجام دهید"""

from  sys import  getsizeof as Gs

print(Gs(list_com))
print(Gs(list_gen))



""" اگر لیست کوچکتر از حافظه در دسترس ماشین در حال اجرا باشد، 
در این صورت list comprehension می تواند سریعتر از عبارت generator معادل ارزیابی شود. 
برای کشف این موضوع، اجازه دهید نتایج حاصل از دو comprehension بالا را جمع بندی کنیم.
 می‌توانید با cProfile.run() اینکار را انجام دهید"""

import cProfile

print(cProfile(sum(list_gen)))
cProfile.run(list_gen)