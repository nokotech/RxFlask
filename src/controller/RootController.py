import os, copy, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from controller.BaseController import BaseController
from model.repository.UserRepository import UserRepository
from model.entity.UserEntity import UserEntity

class RootController(BaseController):

    def __init__(self):
        print('init')
        entity = UserEntity()
        entity.name = "name1"
        entity.age = "age1"

        newEntity = copy.deepcopy(entity)
        newEntity.age = "age2"

        # UserRepository().find(entity)
        # UserRepository().insert(entity)

        # UserRepository().update(entity, newEntity)
        # UserRepository().remove(newEntity)
    
    def getTable(self):
        print('getTable')
        return UserRepository().findAll()
