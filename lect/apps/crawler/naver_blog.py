import requests
from bs4 import BeautifulSoup

query = "파이썬강좌"

def get_search_naver_blog(query, start_page = 1, end_page = None):

    start = (start_page - 1) * 10 + 1

    url = "https://search.naver.com/search.naver?where=post&query={}&start={}".format(query, start)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    print(url)
    result = []
    if end_page is None:
        tot_counts = bs.select("span.title_num")[0].text
        tot_counts = tot_counts.split("/")[-1]
        tot_counts = tot_counts.replace("건", "").replace(",","").strip()
        tot_counts = int(tot_counts)
        end_page = tot_counts / 10

        if tot_counts % 10 > 0 :
            end_page += 1

        if end_page > 900:
            end_page = 900


    lis = bs.select("li.sh_blog_top")
    for li in lis:
        try:
            thumbnail = li.select("img")[0]["src"]
            title = li.select("dl > dt > a")[0]
            summary = li.select("dl > dd.sh_blog_passage")[0].text

            title_link = title["href"]
            title_text = title.text

            result.append((thumbnail, title_text, title_link, summary))
        except:
            continue


    if start_page < end_page:
        start_page += 1
        result.extend(get_search_naver_blog(query, start_page = start_page, end_page = end_page))

    return result 



results = get_search_naver_blog("파이썬강좌", start_page = 1, end_page = 3)

for result in results:
    print(result)