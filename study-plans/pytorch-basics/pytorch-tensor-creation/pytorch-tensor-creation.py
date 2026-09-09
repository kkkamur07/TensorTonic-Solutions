import torch

def create_tensor(method, shape, value=0.0):
    if method == "zeros" : 
        tensorss = torch.zeros(shape)
    elif method == "ones" : 
        tensorss = torch.ones(shape)
    else :
        tensorss = torch.ones(shape) * value

    return tensorss.tolist()
        