from models.base_model import BaseModel

class User(BaseModel):
    """User model class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

if __name__=="__main__":
    new_user=User()
    new_user.last_name='Emmy'
    print(new_user)
    new_user.save()
