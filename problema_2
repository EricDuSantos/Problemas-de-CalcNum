import math
import decimal

iterações = 1
h = 1

def f(x):
    f = (math.e ** x) - 2 * x - 3
    return f

#Chute inicial
x0 = 1
chute = f(x0)
print("O chute inicial é {}.\n".format(chute))

#Achando reta tangente
def derivada(x):
    df = (f(x + h) - f(x))/(h) 
    return df

for i in range(iterações):
    dx = f(x0)/derivada(x0)
    if f(x0-dx)==0:
        print("Raiz é:{}".format(x0-dx))
    else:
        x0 = x0 - dx

print(x0)
