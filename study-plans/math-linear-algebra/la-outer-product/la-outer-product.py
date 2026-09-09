import numpy as np

def outer_product(u, v):
    """
    Returns: float64 matrix of shape (m, n), the outer product u v^T.
    
    Mij = u_i * v_j
    
    """
    u = np.array(u)
    v = np.array(v)

    # converting the vectors on matrices outer products damm. 
    u = u.reshape(-1,1)
    v = v.reshape(1,-1)

    return u @ v