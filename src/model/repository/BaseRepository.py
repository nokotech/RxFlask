class BaseRepository:

    def typeValidate(self, obj, entity):
        if not isinstance(obj, entity):
            raise ValueError("error!")

