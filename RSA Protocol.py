import numpy as np
import time
import math
import sympy
message = "Test testing i hope this works"
p = 248323   #both must be prime
q = 287977
def Ext_Euler_alg(phi, e):   #used to generate the d value
    d = 1    #starts at 1
    check = (e*d) % phi   #check must equal 1 for the d value to be used
    while check != 1:  #runs till a sufficient d value is found
        d += 1
        check = (e*d) % phi
        if d % np.pow(10, min(np.floor(np.log10(d)),6)) == 0:    #ty Blake
            print("d value is: " + str(d), end='\r')   #removes value and reprints it to make it look nicer
    print("d value is: " + str(d))
    return d

def e_generator(phi):
    e_ideal = 65537   #considered the best e value but may make generation time a lot longer
    if math.gcd(e_ideal, phi) == 1:   #checks is 65537 is viable, nearly always is as i believe is prime
        ans = str(input("""Would you like to use the best e value? 
This can make key generation time very long. [Y,N]: """)).strip().lower()
        if ans == "y":
            e = e_ideal  #uses 65537 as the e value
            return e
        else:
            print("Now generating your e value!")
    e = 3  #3 is min, and also a good value to have, is easier to break than 65537
    coprime_check = math.gcd(e, phi)
    while coprime_check != 1:
        e += 2   #usually takes no time, 3,5,7 are all prime which makes it easier
        coprime_check = math.gcd(e, phi)   
        print("e value is: " + str(e), end='\r')
    print("e value is: " + str(e))
    return e

def RSA_key_gen(p, q):
    ti = time.perf_counter()     #used to find the time elapsed
    n = p*q                      #finds the n value by timesing two primes together
    phi = (p-1)*(q-1)            #a simplified way to find the phi value
    e = e_generator(phi)         #applies the e generation function        
    d = Ext_Euler_alg(phi, e)    #applies the d generation function with the newly found e value
    tf = time.perf_counter()  
    print("Time elapsed to generate key is: " + str(round(tf-ti, 4)) + " seconds")#prints time taken for key gen
    return n, e, d
n,e,d = RSA_key_gen(p, q)
print(n,e,d)
        
def public_key_encrypt(message, n, e):
    m_list = []
    c_list = []
    for letter in message:   #converts to ASCII number values
        m_list.append(ord(letter))
    m_len = len(message)
    for i in range(m_len):
        c_list.append((m_list[i]**e % n))










