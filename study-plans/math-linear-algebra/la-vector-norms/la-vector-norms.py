import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    v = np.array(v, dtype = np.float64)

    def l1(v) : 
        return np.sum(np.abs(v))

    def l2(v) : 
        return (np.sum((v**2)))**0.5

    def l_inf(v) : 
        return np.max(np.abs(v))

    return np.array([l1(v), l2(v), l_inf(v)])
    