from requests.api import get
from choicecloths import get_max_pages, extracting_cloths

maxpg = get_max_pages()

extracting_cloths(maxpg)