from threading import Lock
from pymongo import MongoClient

class MongoManager(object):
    _instance = None
    _lock = Lock()
    _db = None

    def __init__(self):
        print('init')
    
    def __new__(cls):
        print('pre new')
        with cls._lock:
            if cls._instance is None:
                cls._preInit(cls)
        return cls._instance
    
    def _preInit(self):
        print('pre init')
        self._instance = super().__new__(self)
        connect = MongoClient('0.0.0.0', 32771)
        self._db = connect.test
        print('db name is = {}'.format(self._db.name))
    
    @property
    def db(self):
        print("getDB {}".format(self._db))
        return self._db