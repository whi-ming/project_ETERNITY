import numpy as np
import random
from functions.helper_functions import newtons_sqrt, abs_diff, mean_custom

"""
Will likely need to build a custom sqrt approximation and other function
"""

def standard_deviation(nums: list[float]) -> float:

    squared_diff = [ (x - mean_custom(nums))**2 for x in nums ]
    ssd = sum(squared_diff)/len(nums)
    
    return newtons_sqrt(ssd) if ssd != 0 else 0.0

if __name__ == "__main__":
    random_floats = [random.uniform(0, 1) for _ in range(100)]
    print(standard_deviation(random_floats))
    print(np.std(random_floats))