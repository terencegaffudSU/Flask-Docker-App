from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h1>'

@app.route("/welcome")
def welcome():
    return "<h1>Welcome to the welcome page</h1>"

if __name__ == "__main__":
    app.run(debug=True)