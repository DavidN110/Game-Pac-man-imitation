import random
import numpy as np

def randomization(n):
    """
    Arg:
    n - an integer
    Returns:
    A - a randomly-generated nx1 Numpy array.
    """
    #Your code here
    A = np.zeros((n, 1)) 
    for i in range(0,n):
        A[i]=random.randint(0,100)
    return print(A)
m = int(input())
randomization(m)