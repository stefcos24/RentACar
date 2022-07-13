import sys
sys.path.append("..")

from fastapi import APIRouter, Depends
from sql import models
from sql.schemas import Reviews
from sql.database import SessionLocal, engine
from sqlalchemy.orm import Session
from errors.error_handlers import raise_id_does_not_exist, get_user_exception
from .user import get_current_user


router = APIRouter(
    prefix='/reviews',
    tags=['reviews'],
    responses={404: {"error": "Reviews not Found"}}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Reviews).all()


@router.get('/users')
async def read_all_by_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    return db.query(models.Reviews).filter(models.Reviews.author_id == user.get("id")). all()


@router.get("/{review_id}")
async def read_review(review_id: int, user:dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    review_model = db.query(models.Reviews)\
        .filter(models.Reviews.id == review_id)\
        .filter(models.Reviews.author_id == user.get("id"))\
        .first()
    if review_model is not None:
        return review_model
    raise raise_id_does_not_exist()


@router.post('/')
async def create_review(review: Reviews, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    review_model = models.Reviews()
    review_model.comment = review.comment
    review_model.rating = review.rating
    review_model.author_id = user.get("id")

    db.add(review_model)
    db.commit()

    return review_model


@router.put('/{review_id}')
async def update_review(review_id: int, review: Reviews, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    review_model = db.query(models.Reviews)\
        .filter(models.Reviews.id == review_id)\
        .filter(models.Reviews.author_id == user.get("id"))\
        .first()

    if review_model is None:
        raise raise_id_does_not_exist()

    review_model.comment = review.comment
    review_model.rating = review.rating

    db.add(review_model)
    db.commit()

    return review_model


@router.delete('/{review_id}')
async def delete_review(review_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    review_model = db.query(models.Reviews)\
        .filter(models.Reviews.id == review_id)\
        .filter(models.Reviews.author_id == user.get("id"))\
        .first()

    if review_model is None:
        raise raise_id_does_not_exist()

    db.query(models.Reviews)\
        .filter(models.Reviews.id == review_id)\
        .delete()

    db.commit()

    return review_model

