import flwr as fl
import sys

# 1. Define the Strategy (FedAvg - Federated Averaging)
strategy = fl.server.strategy.FedAvg(
    fraction_fit=1.0,        # Sample 100% of available nodes
    min_fit_clients=1,       # <--- FIXED: Was 'min_fit_linear'
    min_available_clients=1, # Minimum nodes connected before starting
)

if __name__ == "__main__":
    print("🛡️ [VERITY AGGREGATOR] Central Command Active.")
    print("📡 [VERITY AGGREGATOR] Listening for Trust Nodes on Port 8080...")
    
    # 2. Start the Federated Learning Server
    fl.server.start_server(
        server_address="0.0.0.0:8080",
        config=fl.server.ServerConfig(num_rounds=3),
        strategy=strategy,
    )