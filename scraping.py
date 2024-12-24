import requests
from bs4 import BeautifulSoup

import csv
import datetime

url = "https://news.yahoo.co.jp/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
today = soup.find("section", attrs ={"id":"uamods-topics"})

# ヒットしたTagクラスのインスタンスのリストをリターンする
entries = today.find_all("li")
