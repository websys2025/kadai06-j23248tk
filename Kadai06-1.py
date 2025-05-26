# エンドポイント: getStatsData（https://www.e-stat.go.jp/api/api-info/e-stat-manual3-0#api_2_1）
# 機能: 統計表データ取得。ここでは「家計調査」データを取得する。
# 使用にはアカウント作成・APIキー発行が必要: https://www.e-stat.go.jp/api/api-info/

import requests
import json

API_KEY = "YOUR_API_KEY"
URL = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": API_KEY,
    "statsDataId": "0003217753",  # 家計調査
    "lang": "J",
    "metaGetFlg": "N",
    "cntGetFlg": "N",
    "explanationGetFlg": "N",
    "sectionHeaderFlg": "1"
}

response = requests.get(URL, params=params)
data = response.json()

print(json.dumps(data, indent=2, ensure_ascii=False))

