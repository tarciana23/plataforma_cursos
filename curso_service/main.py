from fastapi import FastAPI, HTTPException
from models import Curso
from schemas import CursoCreate, CursoRead
from database import SessionLocal, engine, Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/cursos", response_model=CursoRead)
def criar_curso(curso: CursoCreate):
    db: Session = SessionLocal()
    db_curso = Curso(**curso.dict())
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso


@app.get("/cursos", response_model=list[CursoRead])
def listar_cursos(categoria: str = None):
    db: Session = SessionLocal()
    
    # Se categoria for fornecida, filtra os cursos pela categoria
    if categoria:
        cursos = db.query(Curso).filter(Curso.categoria == categoria).all()
    else:
        cursos = db.query(Curso).all()  # Retorna todos os cursos, se categoria não for fornecida
    
    if not cursos:
        raise HTTPException(status_code=404, detail="Nenhum curso encontrado.")
    
    return cursos


