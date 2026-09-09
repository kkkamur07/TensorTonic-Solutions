import torch

def compute_gradient(values):
    
    """
    f(x) = x^3 + 2x 
    dy/dx = 3x^2 + 2
    """

    values = torch.tensor(values, requires_grad = True, dtype = torch.float32)
    fun = sum(values**3 + 2*values)

    # calculating the gradient.
    fun.backward()

    return (values.grad).tolist()
