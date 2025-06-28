# AirMove

is a tool that allows you to control your computer using hand gestures tracked by your webcam.
It uses computer vision to detect and track finger movements, enabling you to move the mouse cursor and interact with your system through gestures instead of traditional input devices.

> ✨ Control your computer with gestures — no mouse or touchpad needed!

---

## 🚀 Features

* Move your mouse cursor with your index finger  
* Double click on "pinch in" gesture  
* Cross-platform (macOS, Windows, Linux)  

\* On Linux, some limitations may exist under Wayland. X11 is recommended.

---

## ⚙️ Requirements

* Python 3.8+
* Webcam
* MacOS / Windows / Linux

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/airmove.git
cd airmove
```
### 2. (Recommended) Create a virtual environment on Mac/Linux
```bash
python -m venv .venv
source .venv/bin/activate
```
##### On Windows:
```
.venv\Scripts\activate
```
### 3. Install dependencies
```
pip install opencv-python mediapipe pyautogui  
```
### How to Run
```
python main.py  
```
### How to Stop
if you run in terminal:
```
Ctrl + C
```


