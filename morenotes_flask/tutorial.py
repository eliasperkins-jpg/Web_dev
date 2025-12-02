from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/" methods=["POST, GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("user", name=request. form["name"]))
    return "<h1>Hello!</h1>"

@app.route("/<name>")
def user(name):

    

@app.route("/contact")
def contact():
    return "<p>LEAVE ME ALONE</p>"

    return f"<h1>Hello {name}</h1>"

if __name__ == "__main__":
    app.run(debug=True)