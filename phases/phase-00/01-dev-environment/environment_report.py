import torch
import numpy as np
import sys 
print(f"Python available: {sys.version}")
print (f"Numpy version: {np.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print (f"Interpreter path: {sys.executable}")