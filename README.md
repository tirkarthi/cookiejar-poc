Proof of conccept and slides for chennaipy talk.

* Add below lines to `/etc/hosts`

```
127.0.0.1 example.com
127.0.0.1 badexample.com
```

* Install the requirements from `requirements.txt`
* Run flask app with `python app.py`
* Domain check vulnerability :  `python poc_domain.py <flask_app_port>`
* Path check vulnerability : `python poc_path.py <flask_app_port>`
