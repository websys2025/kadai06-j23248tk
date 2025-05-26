import requests
import json

API_KEY = "YOUR_API_KEY"
URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": API_KEY,
    "statsDataId": "0003217753",
    "lang": "J",
    "metaGetFlg": "N",
    "cntGetFlg": "N",
    "explanationGetFlg": "N",
    "sectionHeaderFlg": "1"
}

response = requests.get(URL, params=params)
data = response.json()

print(json.dumps(data, indent=2, ensure_ascii=False))
