from flask import Flask, request, make_response, session, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    host_url = request.host_url
    print("Current host : ", host_url)
    print(f"Cookies : {request.cookies}")
    res = make_response("hello world")
    res.set_cookie("secret", value=host_url.upper())
    return res

@app.route('/any')
def any_path():
    host_url = request.host_url
    path = request.path
    print("Current host : ", host_url)
    print(f"Cookies : {request.cookies}")
    res = make_response("hello world")
    res.set_cookie("secret_path", value=path.upper(), path="/any")
    return res

@app.route('/anybad')
def anybody_path():
    host_url = request.host_url
    print(f"Anybody Cookies : {request.cookies}, Host URL : {host_url}")
    res = make_response("hello world")
    return res

if __name__ == "__main__":
    app.run(debug=True)
