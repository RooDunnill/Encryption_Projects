import numpy as np
from time import perf_counter
from random import randint
from collections import Counter
import matplotlib.pyplot as plt
class CustomError(Exception):
    pass


def gen_rand_key(n):
    if n <= 0:
        raise ValueError(f"n must be positive")
    if isinstance(n, int):
        lower_bound = 10**(n-1)
        upper_bound = 10**n - 1
        return randint(lower_bound, upper_bound)
    else:
        raise TypeError(f"n cannot be type {type(n)}, must be int")



class Hash:
    def __init__(self, **kwargs):
        self.p = kwargs.get("p", 7)
        self.k = int(kwargs.get("k", 6))
        self.key = int(kwargs.get("key", 382956234980))
        self.key_length = int(len(str(self.key)))
        if self.key_length % self.k == 0:
            string = str(self.key)
            interval = int(self.key_length/self.k)
            self.parameters = [int(string[i:i+interval]) for i in range(0, len(string), interval)]
        else:
            raise CustomError(f"The length of the key must be an integer value of the length of k, where k is the k independent value")
    
    def k_hash(self, vals, text=True):
        start_time = perf_counter()
        def compute_hash(val):
            print(f"\rHasing value: {val} ", end="")
            poly = len(self.parameters)
            hash_value = 0
            poly_change = poly
            for i in self.parameters:
                hash_value += i*(val**poly_change) % self.p
                poly_change -= 1
            hash_value = hash_value % self.p
            return hash_value
        
        if isinstance(vals, int) or isinstance(vals, float):
            hash_value = compute_hash(vals)
            if text:
                print(f"The {self.k} independent hashed value of {vals} is: {hash_value}")
                end_time = perf_counter()
                print(f"Time taken to hash value was: {end_time - start_time:.6f} seconds")
            return hash_value
        
        elif isinstance(vals, np.ndarray) or isinstance(vals, list):
            hash_list = np.array([compute_hash(i) for i in vals])
            if text:
                print(f"The list of {self.k} independent hash inputs and outputs are:\n {np.array(list(zip(vals, hash_list)))}")
                end_time = perf_counter()
                print(f"Time taken to hash list was: {end_time - start_time:.6f} seconds")
            return hash_list
        else:
            raise CustomError(f"The hash input value cannot by of {type(vals)}, it must be a float or an integer.")
    
    def analyse(self, hashed_vals):
        counts = np.zeros(self.p) 
        for val in hashed_vals:
            counts[val] += 1 
        plt.bar(range(self.p), counts, color='skyblue', edgecolor='black')
        plt.xlabel('Bins')
        plt.ylabel('Frequency')
        plt.title(f'Distribution of {self.k}-independent hash value\n with a mod of {self.p} and a key of {self.key}')
        plt.show()
        return counts

    def get_key(self, text=False):
        if text == True:
            print(f"The key for this hash function is: {self.key}")
        return self.key

    def get_k(self, text=False):
        if text == True:
            print(f"The hash function is {self.k} independent")
        return self.k

    def get_p(self, text=False):
        if text == True:
            print(f"The mod value of this function is: {self.p}")
        return self.p



list_vals = np.array(range(100000))
k = 2
k_2_hash = Hash(k=k, key=22, p=2)
hashed_values = k_2_hash.k_hash(list_vals)
k_2_hash.analyse(hashed_values)