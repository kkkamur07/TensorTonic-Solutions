import torch
import torch.nn.functional as F

def compute_loss(pred: torch.Tensor, target: torch.Tensor, method: str, delta: float = 1.0) -> float:
    """
    Returns the mean loss as a Python float.
    """
    pred = torch.tensor(pred, dtype = torch.float32)
    
    def mse(pred, target) : 
        return torch.mean((pred - target) ** 2).item()

    def ce(pred, target) : 
        log_sum = torch.logsumexp(pred, dim = 1) # across the columns

        # Indexing : this is the hard part for me, as need to understand the structure. 
        target_logits = pred[torch.arange(pred.shape[0]), target]
        return torch.mean(log_sum - target_logits).item()

    def huber(pred, target, deltaa) : 
        diff = torch.abs(pred - target)
        loss = torch.where(diff > deltaa, deltaa * (diff - (0.5 * deltaa)), 0.5*(diff**2))
        return torch.mean(loss).item()

    if method == "mse" : 
        return F.mse_loss(pred.float(), target.float()).item()
    elif method == "cross_entropy" : 
        return F.cross_entropy(pred.float(), target.long()).item()

    return F.huber_loss(pred.float(), target.float(), delta=delta).item()


    
        
