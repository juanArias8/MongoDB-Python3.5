class User:
    def __init__(self, name, id, age, email):
        self.name = name
        self.id = id
        self.age = age
        self.email = email

    def user_to_collection(self):
        return {
            "name": self.name,
            "id": self.id,
            "age": self.age,
            "email": self.email
        }

