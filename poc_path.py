import sys
import requests

port = sys.argv[1]

with requests.Session() as s:
    urls = (("http://example.com", "/any"),
            ("http://example.com", "/any"),
            ("http://example.com", "/anybad"))

    for url, path in urls:
        full_url = f'{url}:{port}{path}'
        m = s.get(full_url)
        print(f"Cookies for {full_url} : {m.request.headers.get('Cookie')}")
