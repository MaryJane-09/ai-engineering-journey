import os

print(f"Working Directory: {os.getcwd()}")
print("Files in /app:")
try:
    files = sorted(os.listdir('/workspace'))
    for file in files:
        print(f"  -{file}")
except FileNotFoundError:
    print("  - /workspace directory not found (is it mounted?)")

