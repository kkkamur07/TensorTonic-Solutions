import torch

def activate(x, method="relu"):

    x = torch.tensor(x, dtype = torch.float32)
    
    if method == "relu" : 
        return torch.where(x > 0, x, 0)
    elif method == "sigmoid" : 
        return 1/(1 + torch.exp(-x))
    elif method == "tanh" : 
        return (torch.exp(x) - torch.exp(-x))/(torch.exp(x) + torch.exp(-x))
    else : 
        return torch.where(x > 0, x, 0.01 * x)

        
        