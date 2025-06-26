import cv2
import numpy as np
import os
os.makedirs("output", exist_ok=True)
def remove_borders(image_path, output_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error loading {image_path}")
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        print(f"No borders found in {image_path}")
        return
    all_contours = np.vstack(contours)
    x, y, w, h = cv2.boundingRect(all_contours)
    cropped = image[y:y+h, x:x+w]
    cv2.imwrite(output_path, cropped)
    print(f"Processed {image_path} -> {output_path}")
for filename in os.listdir("input"):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join("input", filename)
        output_path = os.path.join("output", filename)
        remove_borders(input_path, output_path)

print("Border removal complete!")