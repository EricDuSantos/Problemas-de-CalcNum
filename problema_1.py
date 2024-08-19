import math

a = 1
b = 2
iterações = 3

def f(x):
    f = (x**2)*x - 2*x**2 - 5
    return f

#Verificando se f(a)*f(b)>0

print(f(1)*f(2))

c = (a+b)/2

for i in range(1,iterações):
    if f(c)==0:
        print("C = {f} é raiz")
    if f(c)*f(a)<0:
        b = c
    else:
        a = c
    c = (a+b)/2


print(c)
