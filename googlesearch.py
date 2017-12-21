#! python3
# googlesearch.py - Opens several Google search results.

import requests, sys, webbrowser, bs4

# For getting the page and then checking if there is no error such as page not found
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result for links ahving class as 'a'
linkElems = soup.select('.r a')

# Open a browser tab for each result min 5 or for search results having even less results .

numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
