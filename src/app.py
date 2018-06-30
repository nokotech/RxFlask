from flask import Flask, request, abort, jsonify
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

from view.RootView import RootView
from view.WebsocketView import WebsocketView

print("==== " + __name__ + " ====" )
app = Flask(__name__)


@app.route("/")
def index():
    print("access. path = /")
    return RootView().index

@app.route("/regist", methods=["POST"])
def regist():
    print("access. path = /regist")
    return RootView().regist

@app.route('/ws')
def ws():
    print("access. path = /ws")
    if request.environ.get('wsgi.websocket'):
        websocket = request.environ['wsgi.websocket']
        WebsocketView(websocket).start
        while(True):  
            msg = websocket.receive()
            print(msg)
        return
    else:
        abort(404, "Not access type.")

@app.errorhandler(404)
def error_handler(error):
    return "Internal Access Error. <BR>{}".format(error.description)

if __name__ == "__main__":
    app.debug = True
    # app.run(host="0.0.0.0", port=5000)
    server = pywsgi.WSGIServer(("0.0.0.0", 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
