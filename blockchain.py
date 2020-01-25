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
    return sum



print('q = 0.1')
for z in range(0,11):
    print('Con un z='+str(z)+' el valor de P es = '+'%.7f'%attackerSuccesProbablity(0.1,z))

print('q = 0.3')
for z in range(0,51,5):
    print('Con un z='+str(z)+' el valor de P es = '+'%.7f'%attackerSuccesProbablity(0.3,z))

print('Resolviendo para P menos de 0.1%')
vecq=[0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45]
for q in vecq:
    z = -1
    while True:
        z = z + 1
        p = round(attackerSuccesProbablity(q,z), 7)
        if p < 0.0010000:
            break        
    print('Con un q = '+ str(q)+' el valor de z es = '+ str(z))
    
        
    