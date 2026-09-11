import numpy as np

def pairwise_diff(a):
    """Returns: np.ndarray of shape (n, n) where out[i,j] = a[i] - a[j]"""

    a = np.array(a, dtype = np.float64)

    i = a.reshape(-1, 1) # (n,1)
    j = a.reshape(1, -1) # (1,n)

    # This should give us the outer substraction if you will. 
    return i - j