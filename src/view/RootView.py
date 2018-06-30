import os, copy, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from flask import render_template, redirect, url_for

from view.BaseView import BaseView
from controller.RootController import RootController
from model.entity.UserEntity import UserEntity

class Model:
    title="helloworld"
    table=[]

class RootView(BaseView):

    def __init__(self):
        self.controller = RootController()
    
    @property
    def index(self):
        print("RootView.index")
        model = Model()
        model.table = self.controller.getTable()
        return render_template('index.html', model=model, table=model.table)

    @property
    def regist(self):
        print("RootView.regist")
        return redirect(url_for('index'))
