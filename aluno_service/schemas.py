from pydantic import BaseModel, EmailStr

class AlunoCreate(BaseModel):
    nome: str
    email: EmailStr

class AlunoRead(AlunoCreate):
    id: int

    class Config:
        orm_mode = True
