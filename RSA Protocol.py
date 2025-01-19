import numpy as np
import time
import math
import SymPy
p = 7873
q = 7487

def Ext_Euler_alg(phi, e):
    d = 1
    check = (e*d) % phi
    while check != 1:
        d += 1
        check = (e*d) % phi
        if d % 100000 == 0:
            print("d value is currently: " + str(d), end='\r')
    print("d value is currently: " + str(d))
    return d

def e_generator(phi):
    e = 3
    coprime_check = math.gcd(e, phi)
    while coprime_check != 1:
        e += 2
        coprime_check = math.gcd(e, phi)
        print("e value is currently: " + str(e), end='\r')
    print("e value is currently: " + str(e))
    return e

def RSA_key_gen(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e = e_generator(phi)              #dont go lower than 
    d = Ext_Euler_alg(phi, e)
    return n, e, d
n,e,d = RSA_key_gen(p, q)
print(n,e,d)
        







