import numpy as np

class CustomError(Exception):
    pass


class Hash:
    def __init__(self, k, key, **kwargs):
        self.p = kwargs.get("p", 7)
        self.k = int(k)
        self.key = key
        self.key_length = int(len(str(self.key)))
        if isinstance(self.key, int):
            if self.key_length % self.k == 0:
                string = str(self.key)
                self.parameters = [int(string[i:i+self.k]) for i in range(0, len(string), self.k)]
            else:
                raise CustomError(f"The length of the key must be an integer value of the length of k, where k is the k independent value")
        else:
            raise CustomError(f"The key must be an integer")
    
    def hash_function(self, val):
        poly = len(self.parameters)
        hash_value = 0
        poly_change = poly
        for i in self.parameters:
            hash_value += i*(val**poly_change)
            poly_change -= 1
        hash_value = hash_value % self.p
        print(f"The {self.k} independent hashed value of {val} is: {hash_value}")

Hash(k=2, key=896745362738).hash_function(5)
Hash(k=2, key=896745362738).hash_function(665)
Hash(k=2, key=896745362738).hash_function(66)
Hash(k=2, key=896745362738).hash_function(65)