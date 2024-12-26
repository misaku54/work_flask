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
# CSV出力用リスト
today_list = []
index = 1

for entry in entries:
  title = entry.get_text()
  entry_url = entry.find("a").get("href")
  today_list.append([index, title, entry_url])
  index += 1

dt_now = datetime.datetime.now()

with open(str(dt_now.year)+"_"+str(dt_now.month)+"_"+str(dt_now.day)+"_"+str(dt_now.hour)+str(dt_now.minute)+"_NewsTopics.csv", "w") as file:
  writer = csv.writer(file,lineterminator='\n')
  writer.writerows(today_list)
