import math

def attackerSuccesProbablity(q,z):
    p = 1.0 - q
    lamb = z*(q/p)
    sum = 1.0
    
    for k in range(0,z+1):
        poisson = math.exp(-lamb)
        for i in range(1,k+1):
            poisson *= lamb/i
        sum -= poisson*(1-math.pow(q/p,z-k))
    return round(sum,7)

print('Con un q=0.1 los valores de p con z de 0 a 10 es:')
for z in range(0,11):
    print('%.6f'%attackerSuccesProbablity(0.1,z))

        

