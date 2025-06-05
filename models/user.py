from models.base_model import BaseModel

class User(BaseModel):
    """User model class"""
    email=""
    password=""
    first_name=""
    last_name=""

if __name__=="__main__":
    new_user=User()
    new_user.last_name='Emmy'
    print(new_user)
    new_user.save()
