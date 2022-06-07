from pydantic import BaseModel
class num(BaseModel):
    First_Number:int
    Second_Number:int

class Users(BaseModel):
    name : str
    age : str