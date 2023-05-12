import requests
from bs4 import BeautifulSoup #HTMLやXMLファイルからデータを取得し、解析するスクレイピングツール
from time import sleep #スクレイピングはサーバに不可をかけるから休み時間を

#スクレイピング
class Scr():
    def __init__(self, urls):
        self.urls = urls     #初期化　引数はURL
    
    def get_url(self):
        all_text = []        #抽出する文章を格納するリスト
        for url in self.urls:   #複数URLがある場合、一個ずつ対応
            r = requests.get(url)  #requests.get(URL)　データの取得
            c = r.content #バイナリーデータの抽出
            soup = BeautifulSoup(c, "html.parser") # BeautifulSoup(解析対象のHTML/XML, パーサー(解析器) https://ai-inter1.com/beautifulsoup_1/
            article1_content = soup.find_all("p") #すべての<p>を取得
            temp = []
            for con in article1_content:
                out = con.text #疑問なんでバイナリにしてからテキストに戻してるの？？ →　最初からTEXTにしてると上手く動作しない。なぜだろう
                temp.append(out)
            text = ''.join(temp) # .join リスト内を結合
            all_text.append(text)
            sleep(1) #1s毎に実行
        return all_text

sc=Scr(["https://toukei-lab.com/conjoint","https://toukei-lab.com/correspondence"])
print(sc.get_url())



"""
import requests
from bs4 import BeautifulSoup #HTMLやXMLファイルからデータを取得し、解析するスクレイピングツール
from time import sleep

#スクレイピング
class Scr():
    def __init__(self, urls):
        self.urls = urls     #初期化　引数はURL
    
    def get_url(self):
        all_text = []        #抽出する文章を格納するリスト
        for url in self.urls:   #複数URLがある場合、一個ずつ対応
            r = requests.get(url)  #requests.get(URL)　データの取得
            c = r.text #バイナリーデータの抽出
            soup = BeautifulSoup(c, "html.parser") # BeautifulSoup(解析対象のHTML/XML, パーサー(解析器) https://ai-inter1.com/beautifulsoup_1/
            article1_content = soup.find_all("p") #すべての<p>を取得
            temp = []
            for out in article1_content:
                temp.append(out)
            text = ''.join(temp) # .join リスト内を結合
            all_text.append(text)
            sleep(1)
        return all_text

sc=Scr(["https://toukei-lab.com/conjoint","https://toukei-lab.com/correspondence"])
print(sc.get_url())





import requests
from bs4 import BeautifulSoup

url = 'https://toukei-lab.com/conjoint'
res = requests.get(url)
print(res.text)
print(res.content)
"""