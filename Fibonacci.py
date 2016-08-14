a = 0
b = 1
c = 0
serie = [a,b]
num = int(input("Ingrese numero"))

while c < num:
    c=a+b
    if c < num:
        serie.append(c)
        a = b
        b = c
print (serie)


