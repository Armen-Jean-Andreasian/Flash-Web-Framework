# pip install requests
import requests

HOST = "127.0.0.1"
PORT = 8080
SERVER_URL = f"http://{HOST}:{PORT}"
info_url = SERVER_URL + "/data"

response = requests.get(info_url)

# Print all response details
print("Status Code:", response.status_code)
print("Headers:", response.headers)
print("Text:", response.text)
print("Content (Raw Bytes):", response.content)
print("JSON (if applicable):", response.json() if "application/json" in response.headers.get("Content-Type", "") else "Not JSON")
