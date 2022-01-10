from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
num =0
infoset ={}

for num in range(50,55):
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
pprint(infoset)


