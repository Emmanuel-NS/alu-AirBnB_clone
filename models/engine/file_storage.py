import json


class FileStorage:
    __file_path="file.json"
    __objects={}
    def all(self):
        return FileStorage.__objects

    def new(self,obj):
        key=f'{obj.__class__.__name__}.{obj.id}'
        FileStorage.__objects[key]= obj
    
    def save(self):
        dict={}
        for key,obj in FileStorage.__objects.items():
            dict[key]=obj.to_dict()
        
        with open(FileStorage.__file_path,'w') as file:
            json.dump(dict,file)
            
    def reload(self):
        try:
            from models.base_model import BaseModel
            from models.user import User
            with open(FileStorage.__file_path,'r') as file:
                data=json.load(file)
            class_names={'BaseModel':BaseModel,'User':User}
            for key,value in data.items():
                inst=value['__class__']
                if inst in class_names:
                    inst=class_names[inst]
                    FileStorage.__objects[key]=inst(**value)

        except FileNotFoundError:
            pass

