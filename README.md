# Dynamic-Frame-Detection-in-Live-Video-Streams
Python script for real-time video monitoring using OpenCV to detect and count non-blank frames.

This repository contains a Python script that uses OpenCV to monitor a live video feed from a webcam. The script detects and counts non-blank (non-black) frames, making it useful for various real-time video analysis tasks.

## Features

- **Real-Time Video Capture**: Captures video from your webcam using OpenCV.
- **Blank Frame Detection**: Identifies blank (dark) frames by analyzing their mean intensity.
- **Frame Counting**: Starts counting non-blank frames after a period of inactivity.
- **Interactive Display**: Displays the video feed in a window with the option to exit by pressing 'q'.

## Use Cases

- **Security Monitoring**: Detects interruptions or obstructions in camera feeds.
- **Performance Testing**: Ensures reliability and continuity in video capture devices.
- **Interactive Installations**: Triggers events based on visual changes in the video feed.
- **Educational Tool**: Demonstrates basic computer vision concepts using Python.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Real-Time-Video-Monitoring.git

