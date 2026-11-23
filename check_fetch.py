import requests

url = "https://www.genkibatake.co.jp/susaki/market-info/"
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0"
        " Safari/537.36"
    )
}

response = requests.get(url, headers=headers, timeout=20)
print("ステータスコード:", response.status_code)
print("文字数:", len(response.text))
print("ナスが含まれるか:", ("ナス" in response.text) or ("なす" in response.text))
