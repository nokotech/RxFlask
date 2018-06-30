from flask import Flask

from view.RootView import RootView

app = Flask(__name__)

@app.route("/")
def root():
    return RootView().render

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=5000)