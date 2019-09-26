a = int(input("введите число а: "))
b = int(input("введите число b: "))
c = int(input("введите число c: "))
if a>b:
    a,b = b,a
if b>c:
    b,c = c,b
if a>c:
    a,c = c,a
    
print ("a =",a," ","b =",b," ","c =",c)
