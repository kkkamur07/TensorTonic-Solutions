import torch

def reshape_tensor(x, op):
    
    x = torch.tensor(x, dtype = torch.float32)
    
    if op == "flatten" : 
        output = x.flatten()
    elif op == "squeeze" : 
        output = x.squeeze()
    else : 
        output = x.T 

    return output
