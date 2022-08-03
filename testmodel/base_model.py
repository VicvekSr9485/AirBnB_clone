import uuid
import datetime

date_format = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    id = str(uuid.uuid4())
    created_at = datetime.datetime.now()
    updated_at = datetime.datetime.now()


    def __init__(self, id=None, created_at=None, updated_at=None):
        if id is None:
            self.id = BaseModel.id
        if created_at is None:
            self.created_at = BaseModel.created_at
        if updated_at is None:
            self.updated_at = BaseModel.updated_at
    
    def to_dict(self):
        """ dictionary representation of the objects
        """
        dict = {}
        dict.update(self.__dict__)
        dict['created_at'] = dict['created_at'].isoformat()
        dict['updated_at'] = dict['updated_at'].isoformat()
        dict['__class__'] = self.__class__.__name__
        return dict

    def __str__(self):
        """ string format method """
        return "[{}] ({}) ({})".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.datetime.now()

