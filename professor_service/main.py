from fastapi import FastAPI
from models import Professor
from schemas import ProfessorCreate, ProfessorRead
from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/professores", response_model=ProfessorRead)
def criar_professor(professor: ProfessorCreate):
    db: Session = SessionLocal()
    db_professor = Professor(**professor.dict())
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor


@app.get("/professores", response_model=list[ProfessorRead])
def listar_professores():
    db: Session = SessionLocal()
    professores = db.query(Professor).all()
    return professores
