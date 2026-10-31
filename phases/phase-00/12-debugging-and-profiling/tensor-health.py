import torch

def inspect_tensor_health(name, tensor):
    print(f"--- Tensor: {name} ---")
    print(f"Shape:   {tensor.shape}")
    print(f"Dtype:   {tensor.dtype}")
    print(f"Device:  {tensor.device}")
    # Checks if any value in the tensor is NaN
    print(f"Has NaN: {torch.isnan(tensor).any().item()}")
    print()

def main():
    # 1. Create a healthy tensor with finite values
    healthy_tensor = torch.tensor([1.0, 2.5, 3.8, 4.2], dtype=torch.float32, device="cpu")
    
    # 2. Create a tensor containing a NaN value
    nan_tensor = torch.tensor([1.0, float('nan'), 3.8, 4.2], dtype=torch.float32, device="cpu")
    
    # Inspect both tensors
    inspect_tensor_health("Healthy Tensor", healthy_tensor)
    inspect_tensor_health("NaN Tensor", nan_tensor)

if __name__ == "__main__":
    main()
