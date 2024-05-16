from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/emvshop")
@app.route("/emvshop.html")
def emvshop():
    return render_template("emvshop.html")

@app.route("/cart")
@app.route("/cart.html")
def cart():
    return render_template("cart.html")

@app.route("/sites")
@app.route("/sites.html")
def sites():
    return render_template("sites.html")

@app.route("/dcc")
@app.route("/dcc.html")
def dcc():
    return render_template("dcc.html")

@app.route("/blog")
@app.route("/blog.html")
def blog():
    return render_template("blog.html")

@app.route("/contact")
@app.route("/contact.html")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
