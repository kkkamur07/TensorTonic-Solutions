import numpy as np

def scale_cols(data, weights):

    data = np.array(data, dtype = np.float64) # (m, n)
    weights = np.array(weights, dtype = np.float64) # (n)

    weights = weights.reshape(1, -1) # (n, 1)

    return data * weights # (m,n) * (n,1) = (m,n) * (n,n) -> each column being scaled by the same weights. 

    
    