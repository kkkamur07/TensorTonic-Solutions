import numpy as np

def normalize(data):

    data = np.array(data, dtype = np.float64)
    column_mean = np.mean(data, axis = 0)
    column_std = np.std(data, axis = 0)

    column_mean = column_mean.reshape(1, -1)
    column_std = column_std.reshape(1, -1)
    
    return (data-column_mean)/column_std
    
    