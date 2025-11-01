import cv2
from ocr_engine import extract_text
from utils import load_image, save_output

if __name__ == "__main__":
    image_path = "data/input/sample.jpg"
    image = load_image(image_path)

    result_text, boxed_image = extract_text(image)

    save_output(result_text, boxed_image)
    print("✅ OCR Completed. Check 'results' folder.")
