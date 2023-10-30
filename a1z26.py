
"""تابع ord  یونی کد مربوط به هر حرف رو برای ما برمیگرداند
 تابع chr برعکس این رو انجام میدهد"""
def encode(plain):
    return [ord(i) for i in plain ]



def decode(cod):
    return (chr(i) for i in cod)
list=encode('salam')
print(decode(list))