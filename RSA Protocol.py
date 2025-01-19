import numpy as np
import time
import math
p = 7873
q = 7487

def Ext_Euler_alg(phi, e):
    d = 1
    check = (e*d) % phi
    while check != 1:
        d += 1
        check = (e*d) % phi
    return d


def RSA_key_gen(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e = 3                                       #dont go lower than 3
    coprime_check = math.gcd(e, phi)
    while coprime_check != 1:
        coprime_check = math.gcd(e, phi)
        e += 2
    d = Ext_Euler_alg(phi, e)
    return n, e, d
n,e,d = RSA_key_gen(p, q)
print(n,e,d)
        



