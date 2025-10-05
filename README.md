# Mosaic Crack Detection using OpenCV

This project implements a basic image processing pipeline using OpenCV to detect cracks in mosaic images. The goal is to identify and visualize structural cracks in mosaic surfaces by enhancing contrast, detecting edges, and isolating line features. It shows the output in multiple windows.

Dependencies
Ensure you have the following Python packages installed:
1) opencv (for edge detection on the images given)
2) numpy (also for analyzing the image)
3) matplotlib (displaying results in a new window)

Usage:
1) Clone or download the repository.
2) Replace the image_path in the code with the path to your mosaic image.
3) Run the code to get the output of edge detection, and the cracks in the image


Methodology:
1) Preprocessing: Convert to grayscale and enhance contrast using CLAHE.
2) Edge Detection: Apply Canny edge detection to highlight potential cracks.
3) Noise Removal: Morphological transformations clean up the edge map.
4) Line Detection: Hough Transform extracts line segments corresponding to cracks.
5) Binary Conversion: Final image shows detected cracks in white over a black background.
