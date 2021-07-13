from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return "<div><h1>About us</h1><p>lol</p></div>"

if __name__ == "__main__":
    app.run(debug=True)