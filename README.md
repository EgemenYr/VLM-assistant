# VLM Assistant

An edge AI system that detects and tracks whatever you need to find, from any camera you have: a drone, a fixed camera, a phone or a webcam.

**Status:** in development (portfolio project, Oct–Dec 2026)

## Why?

Ayşe, 7, goes missing in a small village. Her family has photos and videos of her, and they know what she was wearing, roughly how tall she is and her shoe size.
Drones start searching. Instead of people watching hours of footage, the system turns that description into a search query and shows the family the people that look like Ayşe, with the frames as evidence.
The family checks the frames, recognizes her, and the search team goes to that spot.

## How it works (planned)

1. **Command:** the user describes what to look for in plain language (e.g. "a small child in a red jacket").
2. **Detect:** a YOLO model finds candidates (e.g. people) in each frame.
3. **Track:** ByteTrack follows each candidate across frames with a stable ID.
4. **Select:** only key frames (a new ID, a confident detection) are sent forward.
5. **Describe:** a small vision-language model (VLM) checks each key frame against the description.
6. **Report:** a structured JSON report lists the matches with evidence frames and timestamps. A human makes the final decision.
7. **Optimize:** models are exported to ONNX and quantized to INT8 to run on edge devices.

## Design principles

- **Any camera:** the video source is a config setting, not code.
- **Any object:** classes, data paths, model paths and thresholds live in `config.yaml`. To find something new, you retrain the detector with your own labeled data. No code changes.
- **Human in the loop:** the system suggests candidates; people decide.
- **No face recognition:** the system does not identify people. It only compares visible attributes such as clothing and size.

Main demo: search and rescue with drone footage (VisDrone dataset).
