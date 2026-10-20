import cv2
import yaml
from pathlib import Path


with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

video_yolu = Path(config["video"]["source"])
cap = cv2.VideoCapture(video_yolu)
if not cap.isOpened():
    print(f"Video açılamadı: {video_yolu}")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
sure = frame_count / fps if fps > 0 else 0

print(f"FPS: {fps}")
print(f"Frame Count: {frame_count}")
print(f"Resolution: {frame_width}x{frame_height}")
print(f"Duration: {sure:.2f} seconds")

cap.release()