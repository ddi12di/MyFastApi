from pydantic import BaseModel



class UserPydantic(BaseModel):
    id: int
    username: str
    phone_number: str


class UserCreate(BaseModel):
    username: str
    phone_number: str

