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
            with open(FileStorage.__file_path,'r') as file:
                data=json.load(file)
            for key,value in data.items():
                FileStorage.__objects[key]=BaseModel(**value)

        except FileNotFoundError:
            pass

