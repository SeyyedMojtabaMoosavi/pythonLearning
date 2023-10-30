#in the nama of God
"""دو راه برای ایجاد یک مجموعه وجود دارد: می‌توانید از تابع set() داخلی استفاده کنید
 یا در عوض، مجموعه‌ای را با آکولاد تعریف کنید. در اینجا چند نمونه آورده شده است"""

set_one=set((0,'ONE',(1,2,3)))
print(set_one)
set_two=set("salm mojtaba") #عدم تکرار پذیری در ست ها....یعنی در تبدیل حروف تکراری را نمی آورد
print((set_two))

set_three={0,(1,2,3),"three"}
print(set_three)

set_four={'salam mojtaba'}
print(set_four)


"""می‌توانید از تابع len() برای بررسی تعداد عناصر 
در یک set استفاده کنید، و همچنین می‌توانید به ترتیب با استفاده 
از عملگرهای in, or, not وجود یک عنصر خاص در یک set را بررسی کنید.

 """

print(len(set_four),len(set_two))
print(0 in set_two)
print(0 not in set_two)
"""می توانید از متد add() برای درج یک عنصر در یک set استفاده کنید. 
اگر می خواهید چندین شی را به طور همزمان در یک set قرار دهید،
 از متد update() استفاده کنید. 
در اینجا چند نمونه آورده شده است"""
set_two.add('salam')
print(set_two)
set_two.update((1,2,4))
print(set_two)

"""اگر می‌خواهید یک عنصر را از یک set حذف کنید، از متد remove() استفاده کنید یا 
اگر آیتم مربوطه در set نباشد، پیام خطا دریافت کنید"""

set_two.remove('salam')
print(set_two)

""" اگر می‌خواهید یک عنصر را از یک set حذف کنید،
 اما اگر آیتم داده شده در set نباشد، نیازی به پیغام خطا ندارید،
 از متد discard() استفاده کنید."""

set_two.discard('salam')
print(set_two)

