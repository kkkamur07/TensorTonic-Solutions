import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    We are going to calculate sample variance so. 
    """

    x = np.array(x)
    mean = np.mean(x)
    normalizing = x - mean
    lenn = len(x)

    var =  (1/(lenn - 1)) * np.sum(normalizing**2)
    std_dev = var ** 0.5

    return {
        "variance" : var, 
        "std_dev" : std_dev
    }
    
    