import base64
from detector import LeafDiseaseDetector

def convert_image_to_base64_and_test(image_bytes: bytes):
    if not image_bytes:
        return None
    base64_string = base64.b64encode(image_bytes).decode('utf-8')
    detector = LeafDiseaseDetector()
    return detector.analyze_leaf_image_base64(base64_string)

def test_with_base64_data(base64_image_string: str):
    detector = LeafDiseaseDetector()
    return detector.analyze_leaf_image_base64(base64_image_string)