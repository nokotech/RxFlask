#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from MongoManager import MongoManager

collect = MongoManager().db.foo
collect.save({'x':10})
collect.save({'x':8})
collect.save({'x':11})

print("find_one = {}".format(collect.find_one))

print("find = ")
for data in collect.find():
    print(data)

print("find_query = ")
for data in collect.find({'x':10}):
    print(data)