import requests
from bs4 import BeautifulSoup

page = 1
url = f"https://search.musinsa.com/category/001004?d_cat_cd=001004&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page={page}&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&shoeSizeOption=&tags=&campaign_id=&timesale_yn=&q=&includeKeywords=&measure="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

def get_max_pages():
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    max_page = int(soup.find("span", {"class":"totalPagingNum"}).get_text())
    return max_page

def extracting_cloths(last_page):
    # for page in range(1, last_page + 1):
    for p in range(1, 3):    
        cloths = []
        res = requests.get(f"https://search.musinsa.com/category/001004?d_cat_cd=001004&brand=&rate=&page_kind=search&list_kind=small&sort=pop&sub_sort=&page={p}&display_cnt=90&sale_goods=&ex_soldout=&color=&price1=&price2=&exclusive_yn=&shoeSizeOption=&tags=&campaign_id=&timesale_yn=&q=&includeKeywords=&measure=")
        print(res.status_code)
        soup = BeautifulSoup(res.text, "html.parser")
        items = soup.find_all("li", {"class":"li_box"})
        for i in items:
            brand = i.find("p", {"class":"item_title"}).string
            name = i.find("p", {"class":"list_info"}).a["title"]
            try:
                price = i.find("p", {"class":"price"}).contents[2]
            except IndexError:
                price = i.find("p", {"class":"price"}).string.strip()
            link = i.find("p", {"class":"list_info"}).a["href"]
            print(brand, name, price, link)
        # return cloths