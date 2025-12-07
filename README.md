# Fruit Color Sorting Robot 🍎🍌🍊

Real-time fruit detection and color-based sorting using YOLOv8 on Raspberry Pi with DOF Robot Arm.

## Team Members
- [Sameeha] - [Role]
- [Nirev] - [Role]
- [Aba] - [Role]

## What It Does
- Detects 7 types of fruits using camera
- Sorts them by color into 4 bins
- Runs on Raspberry Pi at >5 FPS

## Hardware
- Raspberry Pi 4
- DOF Robot Arm
- USB Camera
- 4 colored bins

## Software
- YOLOv8n (trained model)
- OpenCV
- Python 3

## Installation
```bash
pip install -r requirements.txt
```

## How to Run
```bash
python src/main.py
```

## Project Status
- [x] GitHub setup
- [x] Code structure
- [x] Model training started
- [ ] Model training complete
- [ ] Robot integration
- [ ] Testing
- [ ] Demo video

## Deadline
December 12, 2025 at 6:00 PM (Mauritius time)

## Repository Structure
```
fruit-sorting-robot/
├── src/              # Main code
├── models/           # Trained model (best.pt)
├── config/           # Configuration files
├── tests/            # Test scripts
└── presentation/     # Slides and video
```
