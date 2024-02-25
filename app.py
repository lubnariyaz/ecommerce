from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"


try:
    from controller import *
except Exception as e:
    print(e)


app.run(debug=True)
