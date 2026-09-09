import torch

def tensor_op(x, y, op):

    x = torch.tensor(x)
    y = torch.tensor(y)
    
    if op == "add" : 
        tensorss = x + y
    elif op == "matmul" : 
        tensorss = x @ y
    elif op == "multiply" : 
        tensorss = x * y
    elif op == "max" : 
        tensorss = torch.max(x, y)
    else : 
        tensorss = x ** y

    return tensorss.tolist()