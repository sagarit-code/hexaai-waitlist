# models.py
from pydantic import BaseModel, EmailStr

class WaitlistUser(BaseModel):
    name: str | None = None
    email: EmailStr
    role: str
    area: str | None = None
