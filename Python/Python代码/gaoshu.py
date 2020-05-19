import requests
import re
with open('url.txt', 'r+') as f:
    n = 1
    for line in f:
        url = re.findall('https:.*gif', line)
        with open(f"Image/look{n}.jpg", 'wb') as fp:
            fp.write(requests.get(url[0]).content)
            n = n+1
