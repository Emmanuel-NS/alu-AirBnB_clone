import uuid
from datetime import datetime

# from models import storage


class BaseModel:
    def __init__(self,**kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key=='updated_at' or key=='created_at':
                    value=datetime.fromisoformat(value)
                if key=='__class__':
                    continue
                setattr(self,key,value)
        else:
            self.id= str(uuid.uuid4())
            self.created_at= datetime.now()
            self.updated_at= datetime.now()
            # storage.new(self)

    def save(self):
        self.updated_at=datetime.now()
        # storage.save()
    
    def to_dict(self):
        d=self.__dict__.copy()
        d['__class__']=self.__class__.__name__
        d['created_at']=datetime.isoformat(self.created_at)
        d['updated_at']=datetime.isoformat(self.created_at)
        return d

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

