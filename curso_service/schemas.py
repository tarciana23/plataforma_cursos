from pydantic import BaseModel

class CursoCreate(BaseModel):
    nome: str
    categoria: str

class CursoRead(CursoCreate):
    id: int

    class Config:
        orm_mode = True
