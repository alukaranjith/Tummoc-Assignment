from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

app = FastAPI()

# SQLAlchemy setup
engine = create_engine('sqlite:///school.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Database models
class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    teacher_id = Column(Integer, index=True)


Base.metadata.create_all(bind=engine)


# Pydantic models
class TeacherCreate(BaseModel):
    name: str


class TeacherUpdate(BaseModel):
    name: str


class StudentCreate(BaseModel):
    name: str
    teacher_id: int


class StudentUpdate(BaseModel):
    name: str
    teacher_id: int


class TeacherResponse(BaseModel):
    id: int
    name: str


class StudentResponse(BaseModel):
    id: int
    name: str
    teacher_id: int


# Routes
@app.get("/")
def hello_world():
    return "Hello World"


@app.get("/teachers", response_model=List[TeacherResponse])
def get_teachers():
    db = SessionLocal()
    teachers = db.query(Teacher).all()
    db.close()
    return teachers


@app.get("/teachers/{teacher_id}", response_model=TeacherResponse)
def get_teacher(teacher_id: int):
    db = SessionLocal()
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    db.close()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return teacher


@app.post("/teachers", response_model=TeacherResponse)
def create_teacher(teacher: TeacherCreate):
    db = SessionLocal()
    db_teacher = Teacher(name=teacher.name)
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    db.close()
    return db_teacher


@app.put("/teachers/{teacher_id}", response_model=TeacherResponse)
def update_teacher(teacher_id: int, teacher: TeacherUpdate):
    db = SessionLocal()
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db_teacher.name = teacher.name
    db.commit()
    db.refresh(db_teacher)
    db.close()
    return db_teacher


@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int):
    db = SessionLocal()
    db_teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    db.delete(db_teacher)
    db.commit()
    db.close()
    return {"message": "Teacher deleted"}


@app.get("/students", response_model=List[StudentResponse])
def get_students():
    db = SessionLocal()
    students = db.query(Student).all()
    db.close()
    return students
