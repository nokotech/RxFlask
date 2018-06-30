class UserEntity(object):
    name = ""
    age = ""

    @property
    def codable(self):
        return {
            'name': self.name,
            'age': self.age
        }

