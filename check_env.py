import sys
import torch

print(f"Python sürümü: {sys.version}")
print(f"PyTorch sürümü: {torch.__version__}")   
print(f"CUDA kullanılabilir mi: {torch.cuda.is_available()}")
print(f"CUDA sürümü: {torch.version.cuda}") 
print(f"CUDA cihazı adı: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'CUDA cihazı bulunamadı.'}")
print(f"CUDA cihazı özellikleri: {torch.cuda.get_device_properties(0) if torch.cuda.is_available() else 'CUDA cihazı bulunamadı.'}")
print(f"CUDA cihazı toplam bellek: {torch.cuda.get_device_properties(0).total_memory/1024**3:.2f} GB if torch.cuda.is_available() else 'CUDA cihazı bulunamadı.' ")
x = torch.rand(1000, 1000, device='cuda') 
y = x @ x
print(f"Sonuçların cihazı: {y.device} ")
