from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        return redirect(url_for("user", name=request.form["name"]))
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f"<h1>Hello {name}</h1>"

@app.route("/contact")
def contact():
    return render_template("user.html")

    

if __name__ == "__main__":
    app.run(debug=True)

#What does Flask do?**
# Connects websites**
#What are the steps to setting up a Flask project?**
# make the pages, make ways to access websites, trouble shoot**
#How can you reference subpages on your Flask project? (Meaning the difference between the home page and a personal profile)**
# By making different routes for each page**
#What are templates?**
#templates of the pages **