import numpy as np
class CustomError(Exception):
    pass

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
    
    def hash(self, val, text=True):
        if isinstance(val, int) or isinstance(val, float):
            poly = len(self.parameters)
            hash_value = 0
            poly_change = poly
            for i in self.parameters:
                hash_value += i*(val**poly_change)
                poly_change -= 1
            hash_value = hash_value % self.p
            if text == True:
                print(f"The {self.k} independent hashed value of {val} is: {hash_value}")
            return hash_value
        else:
            raise CustomError(f"The hash input value cannot by of {type(val)}, it must be a float or an integer.")
    
    def hash_list(self, input_list, text=True):
        if isinstance(input_list, np.ndarray) or isinstance(input_list, list):
            hash_list = np.array([self.hash(i, text=False) for i in input_list])
            if text == True:
                print(f"The list of hash imputs and outputs are:\n {np.array(list(zip(input_list, hash_list)))}")
            return hash_list
        else:
            raise CustomError(f"The input_list cannot be of the type {type(input_list)}, it must be of the type float or integer.")

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


Hash(k=2, key=896745362738).hash(55)
Hash(k=2, key=896745362738).hash(665)
Hash(k=2, key=896745362738).hash(66)
Hash(k=2, key=896745362738).hash(65)
Hash().hash(7802311)
test = Hash(k=3, key=912369467)
Hash(k=3)
list_vals = [1,2,3,4,5,6,7,8]
Hash(k=3).hash_list(list_vals)