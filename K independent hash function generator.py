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
    plot_count = 0
    p_plot = []
    titles_plot = []
    k_plot = []
    key_plot = []
    plot_all_counts = []
    fig = None
    axs = None
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
            print(f"\rHashing value: {val} ", end="")
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
        
    def custom_hash(self, vals, text=True):
        start_time = perf_counter()
        def compute_hash(val):
            print(f"\rHashing value: {val} ", end="")
            poly = len(self.parameters)
            hash_value = 0
            poly_change = poly
            for i in self.parameters:
                i = (i**2) + i + 1 % i**2 - 1
                hash_value += i*(val**poly_change) % (self.p + i**2 + 1)
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
        Hash.plot_count += 1

        counts = np.zeros(self.p) 
        for val in hashed_vals:
            counts[val] += 1 
        Hash.plot_all_counts.append(counts)
        Hash.k_plot.append(self.k)
        Hash.p_plot.append(self.p)
        Hash.key_plot.append(self.key)

        if Hash.fig is not None:
            plt.close(Hash.fig)

        if Hash.plot_count == 1:
            Hash.fig, Hash.axs = plt.subplots(1, 1, figsize=(4, 4))
            Hash.axs = [Hash.axs]
        else:
            Hash.fig, Hash.axs = plt.subplots(1, Hash.plot_count, figsize=(4 * Hash.plot_count, 4))
            
        for i in range(Hash.plot_count):
            Hash.axs[i].bar(range(Hash.p_plot[i]), Hash.plot_all_counts[i], color='skyblue', edgecolor='black')
            Hash.axs[i].set_title(f'Distribution of {Hash.k_plot[i]}-independent hash value\n with a mod of {Hash.p_plot[i]} and a key of {Hash.key_plot[i]}')
            Hash.axs[i].set_xlabel('Bins')
            Hash.axs[i].set_ylabel('Frequency')
        Hash.fig.tight_layout()
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



list_vals = np.array(range(10000))
k = 3
k_2_hash = Hash(k=2, key=222222, p=4)
hashed_values = k_2_hash.k_hash(list_vals)
k_2_hash.analyse(hashed_values)
custom_hashed_values = k_2_hash.custom_hash(list_vals)
k_2_hash.analyse(custom_hashed_values)
k_3_hash = Hash(k=3, key=222222, p=4)
custom_hashed_values = k_3_hash.custom_hash(list_vals)
k_3_hash.analyse(custom_hashed_values)
plt.show()