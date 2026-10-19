import sys
import torch

print(f"Python sürümü: {sys.version}")
print(f"PyTorch sürümü: {torch.__version__}")   
print(f"CUDA kullanılabilir mi: {torch.cuda.is_available()}")
print(f"CUDA sürümü: {torch.version.cuda}") 

if torch.cuda.is_available():
    device_name = torch.cuda.get_device_name(0)
    total_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
    print(f"CUDA cihazı adı: {device_name}")
    print(f"CUDA cihazı toplam bellek: {total_memory:.2f} GB")
    x = torch.rand(1000, 1000, device='cuda') 
    y = x @ x
    print(f"Sonuçların cihazı: {y.device} ")
else:
    print("CUDA cihazı bulunamadı.")
