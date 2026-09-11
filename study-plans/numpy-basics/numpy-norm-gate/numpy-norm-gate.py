import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""

    x = np.array(X, dtype = np.float64)
    w = np.array(W, dtype = np.float64)

    z = x @ w # (n,d) @ (d,k) -> (n,k)

    # compute L2 Norm

    def l2_row_norm(data) : 
        squared = data ** 2
        sum = np.sum(squared, axis = 1) # hopefully this is the row axis
        norm = sum ** 0.5
        return norm

    row_norm = l2_row_norm(z)

    boolean_mask = (row_norm >= threshold).astype(np.float64).reshape(-1, 1) # (n,1)

    return z * boolean_mask
    