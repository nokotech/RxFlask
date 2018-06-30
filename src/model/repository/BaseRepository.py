import os, copy, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

class BaseRepository:

    def typeValidate(self, obj, entity):
        print("typeValidate. obj={}, entity={}".format(obj, entity))
        if not isinstance(obj, entity):
            raise ValueError("error!")
