import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

num =0
infoset ={}

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    for num in range(55,60):
    
        try:
            saiyourl = 'https://job.mynavi.jp/22/pc/search/corp'+str(num)+'/outline.html'
            with urlopen(saiyourl) as res:
                html = res.read().decode("utf-8")
            # 2. Load a html by BeautifulSoup.
            soup = BeautifulSoup(html, "html.parser")
            # 3. Get items you want.
            companies = soup.select(".heading1-inner h1")
            companies = [t for t in companies]
            company = str(companies[:1])

            descs = soup.select("#corpDescDtoListDescText110")
            descs = [s for s in descs]
            emails =soup.select("#corpDescDtoListDescText130")
            emails = [k for k in emails]

            inf = str(descs[:1])+"/"+str(emails[:1])

            infoset[company] =inf
        except:
            pass
    return json.dumps({
        "company" : company,
        "inf" : inf
    })    

if __name__ == "__main__":
    app.run(debug=True, port=5004)


