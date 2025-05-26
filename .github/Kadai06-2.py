import requests
import json

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=2, ensure_ascii=False))
