import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = r"C:\users\abhyu\Downloads\mosaic_1.jpg"  #replace
img = cv2.imread(image_path, cv2.IMREAD_COLOR)

#grayscaling
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#contrast
clahe = cv2.createCLAHE(clipLimit=60.0, tileGridSize=(10, 10))
enhanced = clahe.apply(gray)

blurred = cv2.GaussianBlur(enhanced, (1, 1), 0)
edges = cv2.Canny(blurred, 30, 100)

#edge detection
edges = cv2.Canny(enhanced, threshold1=300, threshold2=450) 
kernel = np.ones((3, 3), np.uint8)


#noise reduction
kernel = np.ones((3, 3), np.uint8)
edges_clean = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
edges_clean = cv2.morphologyEx(edges_clean, cv2.MORPH_OPEN, kernel)

#line detection
lines = cv2.HoughLinesP(edges_clean, 1, np.pi / 180, threshold=150, minLineLength=10, maxLineGap=10)
crack_lines = np.zeros_like(gray)

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(crack_lines, (x1, y1), (x2, y2), 255, 2)

#monochromatic conversion
_, mono = cv2.threshold(crack_lines, 200, 255, cv2.THRESH_BINARY)


#saving and outputting
cv2.imwrite("cracks_output_b1.png", mono)

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title("Detected Cracks")
plt.imshow(mono, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title("Edges")
plt.imshow(edges, cmap='gray')
plt.axis('off')


plt.tight_layout()
plt.show()
