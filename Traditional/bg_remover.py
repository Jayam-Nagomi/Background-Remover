import cv2
import numpy as np

def BackgroundRemover(image_path):
    image = cv2.imread(image_path)

    #preprocess
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)

    #separate the foreground and find contours
    _, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #create a mask and draw contours on it
    mask = np.zeros_like(gray)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(mask, [cnt], -1, 255, -1)

    #apply mask on original image
    result = cv2.bitwise_and(image, image, mask=mask)

    #save it as png
    bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    bgra[mask == 0] = (0, 0, 0, 0)
    cv2.imwrite("bg_removed.png", bgra)

path = "cup.jpeg"
BackgroundRemover(path)
print("Image Saved Successfully!")

 