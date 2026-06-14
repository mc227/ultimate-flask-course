from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", page_name="index", page_num=2)


@app.route("/home")
def home():
    return render_template("home.html", number=5, data=[{'key':'value1'},{'key':'value2'},{'key':'value3'}])


@app.route("/json")
def json():
    return {'mykey':'myvalue', 'mylist':[5,4,3,2,1]}


@app.route("/dynamic", defaults={"user_input":"mark"})
@app.route("/dynamic/<user_input>")
def dynamic(user_input):
    return f"<h1>this is the user input {user_input}</h1>"

@app.route("/query")
def query():
    first = request.args.get("first")
    second = request.args.get("second")
    return f"<h1>first:{first}, second:{second}</h1>"

@app.route("/form", methods=["GET","POST"])
def form():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        print(user_input)
        return redirect(url_for("home"))
    return '<form method="POST"><input type="text" name="user_input"/><input type="submit"></form>'

@app.route("/acceptjson")
def acceptjson():
    data = request.get_json()
    hello = data['hello']
    mylist = data['list']
    return {'hello':hello, 'mylist': mylist}

@app.route("/error")
def error():
    a = 1/0
    return "error"
