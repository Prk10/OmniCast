import requests

url = "http://127.0.0.1:8080/render"

payload = {
    "content": """
import time
def demo():
    print("This image came from the API!")
""", "format_type": "python"
}

print(f"Sending request to {url}")

try:
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        with open("test_api_image.png", "wb") as f:
            f.write(response.content)
        print("✅ Success!")
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
except requests.exceptions.ConnectionError:
    print("❌ Could not connect. Is 'uvicorn' running?")