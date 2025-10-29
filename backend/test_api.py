import requests
from pathlib import Path
import json

def test_api_endpoint(api_url: str = "http://localhost:8000"):
    test_image = "Media/brown-spot-4 (1).jpg"
    if not Path(test_image).exists():
        print(f"Error: Test image not found at {test_image}")
        return
    with open(test_image, "rb") as img_file:
        files = {"file": (Path(test_image).name, img_file, "image/jpeg")}
        response = requests.post(f"{api_url}/disease-detection-file", files=files)
    print(response.json() if response.status_code == 200 else response.text)

def test_root_endpoint(api_url: str = "http://localhost:8000"):
    response = requests.get(f"{api_url}/")
    print(response.json() if response.status_code == 200 else response.text)

if __name__ == "__main__":
    print("Testing root endpoint...")
    test_root_endpoint()
    print("\nTesting disease detection endpoint...")
    test_api_endpoint()