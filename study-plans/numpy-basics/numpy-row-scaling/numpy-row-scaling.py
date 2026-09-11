import numpy as np

def scale_rows(data, weights):
    data = np.array(data)
    weights = np.array(weights)
    weights = weights.reshape(-1, 1) # in the right shape for element wise multiplication. 
    
    # We are going to do broadcasting to help us with this. 
    return data * weights

    