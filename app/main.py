from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app.models import Base, loanDB
from app.schemas import loanCreate, loanRead

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CI/CD 2 - Lab Exam - G00434671")

@app.get("/health")
def health():
    return{"status": "ok"}

@app.post("/loans", response_model=loanRead, status_code=status.HTTP_201_CREATED)
def add_loan(new_loan: loanCreate, db: Session=Depends(get_db)):
    db_loan= loanDB(**new_loan.model_dump())
    db.add(db_loan)
    try:
        db.commit()
        db.refresh(db_loan)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="This loan ID already exists."
        )
    return db_loan

@app.get("/loans/{id}", response_model=loanRead,)
def get_loans(loan_id: int, db: Session=Depends(get_db)):
    db_loan=db.get(loanDB, loan_id)
    if db_loan is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This loan ID doesn't exist."
        )
    return db_loan

@app.delete("/loans/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_loan(loan_id: int, db: Session=Depends(get_db)):
    db_loan=db.get(loanDB, loan_id)
    if db_loan is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="This loan ID doesn't exist."
            )
    db.delete(db_loan)
    db.commit()
    return
