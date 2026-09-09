import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """
    v = np.array(vectors)
    c = np.array(coefficients)

    result = np.zeros(v[0].shape)
    
    if len(v) != len(c) :
        raise "this cannot be done"
    else : 
        for i in range(len(v)) : 
            result += (v[i] * c[i])

    return result
            
        