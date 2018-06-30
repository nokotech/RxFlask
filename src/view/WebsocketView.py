import os, copy, sys, json
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from flask import render_template, redirect, url_for

from view.BaseView import BaseView
from controller.RootController import RootController
from model.entity.UserEntity import UserEntity


class WebsocketView(BaseView):

    def __init__(self, websocket):
        self.controller = RootController()
        self.websocket = websocket
    
    @property
    def start(self):
        print("RootView.index")
        table = self.controller.getTable()
        items = []

        for item in table:
            del item["_id"]
            items.append( json.loads(json.dumps(item)) )

        self.websocket.send(json.dumps({"items": items}))
        return ""