import requests
from bs4 import BeautifulSoup

url = "https://search.musinsa.com/ranking/best?u_cat_cd="
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

items = soup.find_all("li", {"class":"li_box"})
lst = []
for i in items:
    rank_raw = i.find("p", {"class":"txt_num_rank"}).contents[0]
    rank = int(rank_raw.strip().strip("위"))
    
    name = i.find("p", {"class":"list_info"}).a['title']
    
    try:
        price = i.find("p", {"class":"price"}).contents[2].strip()
    except IndexError:
        price = i.find("p", {"class":"price"}).get_text().strip()
    
    lst.append(f"{rank}, {name}, {price}")

    
    if rank > 19:
        break
print(lst)