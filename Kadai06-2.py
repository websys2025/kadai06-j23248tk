# 概要: 各地の天気予報をJSON形式で提供
# エンドポイント（例）: https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json（東京地方）
# 使用方法: 地域コードを変えることで他の地域も取得可能

import requests
import json

url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"

response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=2, ensure_ascii=False))
