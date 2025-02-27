import numpy as np
from time import perf_counter
from random import randint
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
            poly = len(self.parameters)
            hash_value = 0
            poly_change = poly
            for i in self.parameters:
                hash_value += i*(val**poly_change)
                poly_change -= 1
            hash_value = hash_value % self.p
            return hash_value
        
        if isinstance(vals, int) or isinstance(vals, float):
            hash_value = compute_hash(vals)
            if text:
                print(f"The {self.k} independent hashed value of {vals} is: {hash_value}")
                end_time = perf_counter()
                print(f"Time taken to hash value was: {end_time - start_time:.4f} seconds")
            return hash_value
        
        elif isinstance(vals, np.ndarray) or isinstance(vals, list):
            hash_list = np.array([compute_hash(i) for i in vals])
            if text:
                print(f"The list of {self.k} independent hash inputs and outputs are:\n {np.array(list(zip(vals, hash_list)))}")
                end_time = perf_counter()
                print(f"Time taken to hash list was: {end_time - start_time:.4f} seconds")
            return hash_list
        else:
            raise CustomError(f"The hash input value cannot by of {type(vals)}, it must be a float or an integer.")
    

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


Hash(k=2, key=896745362738).k_hash(55)
Hash(k=2, key=896745362738).k_hash(665)
Hash(k=2, key=896745362738).k_hash(66)
Hash(k=2, key=896745362738).k_hash(65)
Hash().k_hash(7802311)
test = Hash(k=3, key=912369467)
Hash(k=3)
list_vals = [1,2,3,4,5,6,7,8]
Hash(k=3).k_hash(list_vals)
Hash(k=10, key=gen_rand_key(100)).k_hash(list_vals)
k = 20
Hash(k=k, key=gen_rand_key(k**2)).k_hash(list_vals)