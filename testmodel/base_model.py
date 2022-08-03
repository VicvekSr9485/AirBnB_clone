import uuid
import datetime

class BaseModel:
    id = str(uuid.uuid4())
    create_at = datetime.datetime.now()
    update_at = datetime.datetime.now()

    def __init__(self, id, create_at=None, update_at=None):
        self.id = id
        self.create_at = create_at
        self.update_at = update_at
    
    def to_dict(self):
        return {
            'id': self.id,
            'create_at': self.create_at,
            'update_at': self.update_at
        }
    
    def __str__(self):
        return f'BaseModel({self.id}, {self.__dict__})'

    def save(self):
        self.update_at = datetime.datetime.now()
        return self.update_at
        
