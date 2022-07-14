from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/article_list')
def article_list():
    return render_template("article_list.html")