from models.base_model import BaseModel
class Review(BaseModel):
    """Review model class"""
    place_id = ""
    user_id = ""
    text = ""