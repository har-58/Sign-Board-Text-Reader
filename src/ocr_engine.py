import easyocr
import cv2

reader = easyocr.Reader(['en'])

def extract_text(image):
    results = reader.readtext(image)
    text_data = []

    for (bbox, text, prob) in results:
        text_data.append(text)
        pts = bbox
        cv2.rectangle(image, tuple(pts[0]), tuple(pts[2]), (0,255,0), 2)
        cv2.putText(image, text, tuple(pts[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)

    return "\n".join(text_data), image
