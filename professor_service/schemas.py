from pydantic import BaseModel

class ProfessorCreate(BaseModel):
    nome: str
    especialidade: str

class ProfessorRead(ProfessorCreate):
    id: int

    class Config:
        orm_mode = True
