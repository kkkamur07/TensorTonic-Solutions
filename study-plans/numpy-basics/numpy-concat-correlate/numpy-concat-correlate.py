import numpy as np

def compare_correlations(a: list, b: list) -> np.ndarray:
    """
    Returns float64 correlation matrices for a, b, and their combined rows.
    """
    a = np.array(a, dtype = np.float64)
    b = np.array(b, dtype = np.float64)

    # so we need to correlate columns not rows. 
    concated = np.concatenate([a,b], axis = 0)
    
    a_corr = np.corrcoef(a, rowvar = False)
    b_corr = np.corrcoef(b, rowvar = False)
    corr_generally = np.corrcoef(concated, rowvar = False)

    return np.stack([a_corr, b_corr, corr_generally])
    