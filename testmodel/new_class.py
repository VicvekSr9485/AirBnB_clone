from base_model import BaseModel

class NewClass(BaseModel):
    def __init__(self):
        super(NewClass, self).__init__()
        self.id = id


print(NewClass.id)
print(NewClass.create_at)
print(NewClass.update_at)

NewClass.save()
print(NewClass.update_at)


class NewClass2(BaseModel):
    def __init__(self):
        super(NewClass2, self).__init__()
        


print(NewClass2.id)
print(NewClass2.create_at)
print(NewClass2.update_at)