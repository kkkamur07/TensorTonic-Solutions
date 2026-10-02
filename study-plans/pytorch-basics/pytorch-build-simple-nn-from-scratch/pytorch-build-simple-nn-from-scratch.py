import torch
import torch.nn as nn

# Inherits from nn.Module
class SimpleNet(nn.Module):
    
    def __init__(self, in_features: int, hidden_size: int, out_features: int):
        super().__init__()

        self.layers = nn.Sequential(
            nn.Linear(in_features, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, out_features)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Returns a float32 tensor of shape (batch, out_features).
        """
        return self.layers(x)
        
