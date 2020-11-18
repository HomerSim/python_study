import requests
from bs4 import BeautifulSoup
import re

def search_google(keyword, start_page, end_page = None):
    keyword = "리눅스 magnet:?xt="
    url = "https://www.google.com/search?q={0}&oq={0}".format(keyword)

    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
    r = requests.get(url, headers= header)
    bs = BeautifulSoup(r.text, 'lxml')
    links = bs.select("div.g > div.rc > div > a")

    results = []
    if end_page is None:
        counts = bs.select("div#result-stats")[0].text.replace("검색결과 약","").replace("개","").replace(",","").strip().split("(")[0]
        end_page = int(int(counts) / 10)

        if end_page > 20:
            end_page = 20

    for a in links:
        href = a["href"]
        text = a.select("h3")
        if (len(text) <= 0):
            continue

        title = text[0].text

        try:
            r = requests.get(href)
            bs = BeautifulSoup(r.text, "lxml")
            magnets = bs.find_all("a", href=re.compile(r'magnet:\?xt=*'))

            if len(magnets) > 0:
                magnet = magnets[0]["href"]
                results.append((title, magnet))
        except:
            pass
    
    if start_page < end_page:
        start_page+=10
        results.extend(search_google(keyword, start_page, end_page=end_page))

    return results

results = search_google("리눅스", 0)
for r in results:
    print(r)    
