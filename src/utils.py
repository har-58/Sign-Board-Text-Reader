import cv2
import os

def load_image(path):
    return cv2.imread(path)

def save_output(text, image):
    os.makedirs("results", exist_ok=True)
    os.makedirs("data/output", exist_ok=True)

    with open("results/recognized_text.txt", "w") as f:
        f.write(text)

    cv2.imwrite("data/output/boxed_output.jpg", image)
