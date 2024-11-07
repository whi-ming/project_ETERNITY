import numpy as np
from functools import reduce

def mean_custom(nums: list[float]) -> float:
    return reduce(lambda x, y: x + y, nums) / len(nums)

def newtons_sqrt(a: float, TOL : int = 1e-8, N_max : int = 20) -> float:

    if (not a or a < 0):
        print("ENCOUNTERED NON-POSITIVE/ZERO SQRT")
        return 0.0
    
    # Newton's Sqrt approximation
    def g(x : float, a : float):
        return 0.5 * (x + a / x)
    
    n = 0 #counter
    x_n = a / 2.0 #initial guess
    x_array = np.array(x_n).reshape(1,1) #iteration logger
    rel_increment = np.inf #Approximation Error

    while (n < N_max and rel_increment > TOL):
        x_n = g(x_n, a)
        rel_increment = abs_diff(x_n, x_array[-1][0]) / x_n #don't need to take abs of x_n as it will never be < 0!
        x_array = np.vstack((x_array, x_n))


    return x_array[-1][0]

def abs_diff(a: float, b: float) -> float:
    res = (a - b)
    return -(res) if res < 0 else res


if __name__ == "__main__":
    #test = [1,2,3,4,5]
    test = 210398491384
    print(newtons_sqrt(test))
    print(np.sqrt(test))