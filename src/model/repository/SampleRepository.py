#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, copy, sys
from MongoManager import MongoManager
from BaseRepository import BaseRepository
from SampleEntity import SampleEntity #TODO: move

class SampleRepository(BaseRepository):
    
    _sampleCollect = None
    
    def __init__(self):
        print('init')
        self._sampleCollect = MongoManager().db.sample
        print("find = ")
        for data in self._sampleCollect.find():
            print(data)

    def insert(self, obj):
        print("insert. {}".format(obj))
        self.typeValidate(obj, SampleEntity)
        self._sampleCollect.save(obj.codable)
    
    def update(self, obj, newObj):
        print("update. {} {}".format(obj.codable, newObj.codable))
        self.typeValidate(obj, SampleEntity)
        data = self._sampleCollect.find_one(obj.codable)
        data['age'] = newObj.age
        self._sampleCollect.save(data)

    def find(self, obj):
        print("find. {}".format(obj))
        self.typeValidate(obj, SampleEntity)
        for data in self._sampleCollect.find(obj.codable):
            print(data)
    
    def remove(self, obj):
        print("remove. {}".format(obj))
        self.typeValidate(obj, SampleEntity)
        self._sampleCollect.remove(obj.codable)


entity = SampleEntity()
entity.name = "name1"
entity.age = "age1"

newEntity = copy.deepcopy(entity)
newEntity.age = "age2"

SampleRepository().find(entity)
SampleRepository().insert(entity)

SampleRepository().update(entity, newEntity)
SampleRepository().remove(newEntity)

