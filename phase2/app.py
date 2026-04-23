from flask import Flask, request

app = Flask(__name__)


@app.route("/about")
def about():
    return "This is Euler's site"


@app.route("/")
def home():
    return """
    <h1>My server<h1>
    <form method="Post" action="/greet">
        <input name ="username" placeholder="Your Name">
        <button type="submit">Submit</button>
    </form>
    """


@app.route("/greet", methods=["POST"])
def greet():
    username = request.form["username"]
    return f"<h1>Hello, {username}!<h1>"


@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}!"


if __name__ == "__main__":
    app.run(debug=True)
