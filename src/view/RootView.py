import os, copy, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from flask import render_template

from view.BaseView import BaseView
from controller.RootController import RootController

class RootView(BaseView):

    def __init__(self):
        self.controller = RootController()
        # pass

    @property
    def render(self):
        return render_template('index.html', title="helloworld")