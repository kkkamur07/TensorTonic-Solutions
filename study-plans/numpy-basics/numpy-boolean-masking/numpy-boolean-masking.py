import numpy as np

def row_summary(data, threshold):
    """
    Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered

    Builds a three filtered view of 2D array : 
    - element level boolean mask
    - rows kept when element exceeds any threshold
    - rows keps when all elements exceeds any threshold
    """

    data = np.array(data, dtype = np.float64)
    zeros = np.zeros_like(data)

    element_level_mask = np.where(data > threshold, 1, 0)
    any_row_filter = np.where(np.any(data > threshold, axis=1, keepdims=True), data, zeros)
    all_row_filter = np.where(np.all(data > threshold, axis=1, keepdims=True), data, zeros)
    
    return element_level_mask, any_row_filter, all_row_filter
    
    