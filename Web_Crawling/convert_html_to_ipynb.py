from bs4 import BeautifulSoup
import json
import urllib.request

url = 'file:///D:/Git-Hub/Data%20and%20Jupyter%20Notebook%20Files/KGB%20-%20Data%20Science/Web%20Crawling/1.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11'
                  '(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

req = urllib.request.Request(url, headers=headers)
page = urllib.request.urlopen(req)
text = page.read()

soup = BeautifulSoup(text, 'lxml')
create_nb = {
    'nbformat': 4,
    'nbformat_minor': 2,
    'cells': [],
    'metadata': {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    }
}

cell = {
    'metadata': {},
    'outputs': [],
    'source': [soup.get_text()],
    'execution_count': None,
    'cell_type': 'code'
}
create_nb['cells'].append(cell)

with open('Python_MANOVA.ipynb', 'w') as jynotebook:
    jynotebook.write(json.dumps(create_nb))

create_nb
