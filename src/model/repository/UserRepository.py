import os, copy, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from model.repository.MongoManager import MongoManager
from model.repository.BaseRepository import BaseRepository
from model.entity.UserEntity import UserEntity

class UserRepository(BaseRepository):
    
    _userCollect = None
    
    def __init__(self):
        print('init')
        self._userCollect = MongoManager().db.user

    def insert(self, obj):
        print("insert. {}".format(obj))
        self.typeValidate(obj, UserEntity)
        self._userCollect.save(obj.codable)
    
    def update(self, obj, newObj):
        print("update. {} {}".format(obj.codable, newObj.codable))
        self.typeValidate(obj, UserEntity)
        data = self._userCollect.find_one(obj.codable)
        data['age'] = newObj.age
        self._userCollect.save(data)

    def find(self, obj):
        print("find. {}".format(obj))
        self.typeValidate(obj, UserEntity)
        for data in self._userCollect.find(obj.codable):
            print(data)
    
    def findAll(self):
        print("findAll.")
        for data in self._userCollect.find():
            print(data)
    
    def remove(self, obj):
        print("remove. {}".format(obj))
        self.typeValidate(obj, UserEntity)
        self._userCollect.remove(obj.codable)
