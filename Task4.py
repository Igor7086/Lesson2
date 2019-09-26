a = int(input ("Введите длину первой стороны: "))
b = int(input ("Введите длину второй стороны: "))
c = int(input ("Введите длину третьей стороны: "))
if (a+b>c) and (b+c>a) and (a+c>b):
    print ("YES")
else:
    print ("NO")
