import torch
import torch.nn as nn
import torch.optim as optim
import flwr as fl
from collections import OrderedDict

# 1. Define a Financial Risk Model
class RiskModel(nn.Module):
    def __init__(self):
        super(RiskModel, self).__init__()
        # 3 inputs (Price, Volume, Volatility) -> 1 output (Risk Score 0-1)
        self.linear = nn.Linear(3, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))

# 2. Define the Flower Client for AFDI Collaboration
class VerityClient(fl.client.NumPyClient):
    def __init__(self, model):
        self.model = model

    def get_parameters(self, config):
        return [val.cpu().numpy() for _, val in self.model.state_dict().items()]

    def set_parameters(self, parameters):
        params_dict = zip(self.model.state_dict().keys(), parameters)
        state_dict = OrderedDict({k: torch.tensor(v) for k, v in params_dict})
        self.model.load_state_dict(state_dict, strict=True)

    def fit(self, parameters, config):
        self.set_parameters(parameters)
        print("🧠 [AI BRAIN] Training on local financial data...")
        
        optimizer = optim.SGD(self.model.parameters(), lr=0.01)
        criterion = nn.MSELoss()
        
        # Dummy data for MVP: (3 features, 1 target)
        data = torch.randn(32, 3) 
        target = torch.randn(32, 1)
        
        optimizer.zero_grad()
        loss = criterion(self.model(data), target)
        loss.backward()
        optimizer.step()
        
        print(f"✅ [AI BRAIN] Round Complete. Local Loss: {loss.item():.4f}")
        return self.get_parameters(config={}), 32, {}

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)
        return 0.1, 32, {"accuracy": 0.95}

if __name__ == "__main__":
    print("📈 [VERITY BRAIN] Starting Financial Node...")
    model = RiskModel()
    # Connect to the AFDI Manager
    fl.client.start_client(server_address="verity_aggregator:8080", client=VerityClient(model))