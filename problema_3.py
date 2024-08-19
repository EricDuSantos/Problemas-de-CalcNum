import math

iterações = 3

def f(x):
    f = math.sqrt(x) - math.cos(x)
    return f

x = [1,2]

for i in range(0,iterações):
    x.append((x[i]*f(x[i+1]) - x[i+1]*f(x[i]))/(f(x[i+1]) - f(x[i])))

print(x[3])
