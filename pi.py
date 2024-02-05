from decimal import Decimal, getcontext

getcontext().prec = 100

a = Decimal(-1)
pi = Decimal(0)

while True:
    a += 2
    if (a - 1) % 4 == 0:
        pi += 1 / a
    else:
        pi -= 1 / a
    if (a - 1) % 10000 == 0:
        print(pi * 4)
