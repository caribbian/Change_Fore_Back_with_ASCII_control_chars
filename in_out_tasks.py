# list=['randommail@pymail.ru', 'pythonist_2000', '01.02.2003']
# for i in map(float, input().split()):
#     print("{:<5.2f} {:<.2f}".format(i, i**2))

# mail, login, date=input().split()
# print('{:<35}'.format(mail), '{:>20}'.format(login), '{:>10}'.format(date))

# print("{:<35} {:>20} {:>10}".format((s := input().split())[0], s[1], s[-1])) # var 2

# 2.67 4.94 4.49 8.48 5.25
# import math
# for i in map(float, input().split()):
#     print("{:<5.2f} {:>5.2f}".format(i, math.log(i)))

# ВАЗ 2107 фиолетовый 230000р
# Лада Приора черный 342500р
    
# mark, model, color, price=input().split()
# mark2, model2, color2, price2=input().split()
# print('{:<15}'.format(mark), '{:>15}'.format(model), '{:>15}'.format(color), '{:>15}'.format(price))
# print('{:<15}'.format(mark2), '{:>15}'.format(model2), '{:>15}'.format(color2), '{:>15}'.format(price2))

# a, b, c = map(float, input().split())
# print('{:.2f}'.format(2*a+10*b+5*c))

# import math
# def ctg(n):
#     return 1/math.tan(n)
# x=float(input())
# y=(1/3*math.sin(x)**5*math.tan(3*x))**(1/9)/ctg(math.cos(128*x/93))
# print('%.2f' % y)

# import math
# x=float(input())
# y=math.sqrt(x+77)*math.sqrt(abs(x+23))-math.sqrt(x-1+math.sqrt(x**4))
# print('%.2f' % y)

x, y=input().split('.')
z=''
if len(y)<2:
    z='0'
print(x+' руб. '+y+z+' коп.')