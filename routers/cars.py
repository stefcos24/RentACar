import sys

sys.path.append("..")

from fastapi import APIRouter, Depends
from sql import models
from sql.database import SessionLocal, engine
from sql.schemas import Cars, CreateCars
from sqlalchemy.orm import Session
from errors.error_handlers import raise_id_does_not_exist, get_user_exception
from .user import get_current_user

router = APIRouter(
    prefix='/cars',
    tags=['cars'],
    responses={404: {"error": "Car not Found"}}
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
    return db.query().all()


@router.get('/users')
async def read_all_by_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    return db.query(models.Cars).filter(models.Cars.user_rented_id == user.get("id")). all()


@router.get('/{car_id}')
async def get_car_id(car_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    car_model = db.query(models.Cars)\
        .filter(models.Cars.id == car_id)\
        .filter(models.Cars.user_rented_id == user.get("id"))\
        .first()
    if car_model is not None:
        return car_model
    
    raise raise_id_does_not_exist()


@router.post('/')
async def add_cars(car: Cars, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is not None:

        car_model = models.Cars()
        car_model.brand = car.brand
        car_model.model = car.model
        car_model.year = car.year
        car_model.engine_capacity = car.engine_capacity
        car_model.gearbox = car.gearbox
        car_model.fuel = car.fuel
        car_model.doors = car.doors
        car_model.seats = car.seats
        car_model.price = car.price
        car_model.ac = car.ac
        car_model.abs = car.abs
        car_model.user_rented_id = None

        db.add(car_model)
        db.commit()

        return car_model
    
    raise raise_id_does_not_exist()


@router.put('/{car_id}')
async def update_cars(car_id: int, car: Cars, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is not None:

        car_model = db.query(models.Cars)\
            .filter(models.Cars.id == car_id)\
            .first()

        if car_model is None:
            raise raise_id_does_not_exist()
    
        car_model.brand = car.brand
        car_model.model = car.model
        car_model.year = car.year
        car_model.engine_capacity = car.engine_capacity
        car_model.gearbox = car.gearbox
        car_model.fuel = car.fuel
        car_model.doors = car.doors
        car_model.seats = car.seats
        car_model.price = car.price
        car_model.ac = car.ac
        car_model.abs = car.abs
        car_model.user_rented_id = car.user_rented_id

        db.add(car_model)
        db.commit()

        return car_model
    
    raise raise_id_does_not_exist()

@router.delete('/{car_id}')
async def delete_cars(car_id: int, user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is not None:

        car_model = db.query(models.Cars).filter(models.Cars == car_id).first()

        if car_model is None:
            raise raise_id_does_not_exist

        db.query(models.Cars).filter(models.Cars.id == car_id).delete()

        db.commit()

        return {"Successfully deleted"}
    
    raise raise_id_does_not_exist()
