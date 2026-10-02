import torch
import torch.nn as nn

class CustomLinear(nn.Module):
    def __init__(self, in_features: int, out_features: int):
        super().__init__()

        weights = torch.randn(out_features, in_features)
        bias = torch.randn(out_features)

        self.weight = nn.Parameter(weights)
        self.bias = nn.Parameter(bias)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor of shape (batch, out_features).
        """

        # This is the one dimensional bias broadcast across the rows. 
        return x @ self.weight.T + self.bias
