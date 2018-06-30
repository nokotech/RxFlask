from flask import Flask

from view.RootView import RootView

app = Flask(__name__)

@app.route("/")
def index():
    return RootView().index

@app.route("/regist", methods=["POST"])
def regist():
    return RootView().regist

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)