import numpy as np
import time
import math
import sympy
p = 7873
q = 7487
def Ext_Euler_alg(phi, e):
    d = 1
    check = (e*d) % phi
    while check != 1:
        d += 1
        check = (e*d) % phi
        if d % 100000 == 0:
            print("d value is: " + str(d), end='\r')
    print("d value is: " + str(d))
    return d

def e_generator(phi):
    e_ideal = 65537
    if math.gcd(e_ideal, phi) == 1:
        ans = str(input("""Would you like to use the best e value? 
This can make key generation time very long. [Y,N]: """)).strip().lower()
        if ans == "y":
            e = e_ideal
            return e
        else:
            print("Now generating your e value!")
    e = 3
    coprime_check = math.gcd(e, phi)
    while coprime_check != 1:
        e += 2
        coprime_check = math.gcd(e, phi)
        print("e value is: " + str(e), end='\r')
    print("e value is: " + str(e))
    return e

def RSA_key_gen(p, q):
    ti = time.perf_counter()
    n = p*q
    phi = (p-1)*(q-1)
    e = e_generator(phi)              #dont go lower than 
    d = Ext_Euler_alg(phi, e)
    tf = time.perf_counter()
    print("Time elapsed to generate key is: " + str(round(tf-ti, 4)) + " seconds")
    return n, e, d
n,e,d = RSA_key_gen(p, q)
print(n,e,d)
        







