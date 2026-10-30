import time
import torch
# Running on cpu CUDA not available
a = torch.rand(800, 90)
b = torch.rand(90, 500)

start = time.perf_counter()
result = torch.matmul(a, b)
end = time.perf_counter()

total_time = end - start
print(f"Total Time: {total_time}")
print("Output Shape:", result.shape)
print( torch.cuda.is_available())