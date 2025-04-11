from fastapi import FastAPI
from models import Aluno
from schemas import AlunoCreate, AlunoRead
from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/alunos", response_model=AlunoRead)
def criar_aluno(aluno: AlunoCreate):
    db: Session = SessionLocal()
    db_aluno = Aluno(**aluno.dict())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno

@app.get("/alunos", response_model=list[AlunoRead])
def listar_alunos():
    db: Session = SessionLocal()
    alunos = db.query(Aluno).all()  
    return alunos