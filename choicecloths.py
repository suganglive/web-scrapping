import requests
from bs4 import BeautifulSoup

page = 1
url = f"https://search.musinsa.com/category/001004?d_cat_cd=001004&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page={page}&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&shoeSizeOption=&tags=&campaign_id=&timesale_yn=&q=&includeKeywords=&measure="

def get_max_pages():
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    max_page = int(soup.find("span", {"class":"totalPagingNum"}).get_text())
    return max_page

def extracting_cloths(last_page):
    for page in range(1, last_page + 1):
        cloths = []
        res = requests.get("https://search.musinsa.com/category/001004?d_cat_cd=001004&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page={page}&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&shoeSizeOption=&tags=&campaign_id=&timesale_yn=&q=&includeKeywords=&measure=") 
        print(res.status_code)
        if page >10:
            break 
        return cloths