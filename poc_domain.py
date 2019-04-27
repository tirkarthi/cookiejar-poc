import sys
import requests

port = sys.argv[1]

with requests.Session() as s:
    urls = ["http://example.com",
            "http://example.com",
            "http://badexample.com"]

    for url in urls:
        full_url = f'{url}:{port}'
        m = s.get(full_url)
        print(f"Cookies for {url} : {m.request.headers.get('Cookie')}")
