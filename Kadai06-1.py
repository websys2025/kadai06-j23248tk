# e-Stat APIを使って「家計調査（家計収支編）」の統計データを取得するプログラム
# データセット: statsDataId='0003003309'（二人以上の世帯・家計収支編）

import requests
import json

API_KEY = '2742a864c28868cc67c6c153a81f3cdd88886f1e'
stats_data_id = '0003003309'

url = 'https://api.e-stat.go.jp/rest/3.0/app/json/getStatsList'
params = {
    'appId': API_KEY,
    'searchWord': '家計調査',
    'limit': 10
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(json.dumps(data, indent=2, ensure_ascii=False))
else:
    print("データ取得に失敗しました")
