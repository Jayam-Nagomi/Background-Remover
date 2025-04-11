# Traditional Background Remover

This is a basic traditional background remover script using OpenCV.  
It works by converting the image to grayscale, applying blur, detecting contours, and masking out the background.

## 🧪 Test Info

- The script has been tested on a sample image (`cup.jpeg`) and the output (`bg_removed.png`) is included.
- Note: This method is highly image-specific. It **will not work reliably** on other images without **custom adjustments** to parameters like blur, threshold, and contour area.

## 🖼️ Example

### Input Image

![Input](Traditional/cup.jpeg)

### Output Image

![Output](Traditional/bg_removed.png)

## 📦 Prerequisites

Make sure you have Python and the required packages installed:

```bash
pip install opencv-python numpy
```
