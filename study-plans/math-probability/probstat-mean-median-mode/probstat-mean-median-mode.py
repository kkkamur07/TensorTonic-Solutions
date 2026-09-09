import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    x = np.array(x)
    # Smallest value with the highest frequency. 
    mode, freq = Counter(x).most_common(n=1)[0]

    return {
        "mean" : np.mean(x), 
        "median" : np.median(x), 
        "mode" : mode
    }