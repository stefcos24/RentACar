from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class CreateUser(BaseModel):
    username: str
    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    email: Optional[str]
    password: str = Field(min_length=7)
    year_born: int = Field(gt=1950, lt=(date.today().year + 1) - 18)
    phone_number: str


class Cars(BaseModel):
    brand: str = Field(min_length=1)
    model: str = Field(min_length=1)
    year: int = Field(gt=1980, lt=date.today().year)
    engine_capacity: int = Field(gt=800)
    gearbox: str = Field(min_length=1)
    fuel: str = Field(min_length=1)
    doors: int = Field(gt=2, lt=6)
    seats: int = Field(gt=3, lt=10)
    price: float = Field(gt=1)
    ac: bool = Field()
    abs: bool = Field()
    user_rented_id: Optional[int] = None


class Reviews(BaseModel):
    rating : int = Field(gt=0, lt=6)
    comment : str = Field(min_length=1)


class CreateCars(Cars):
    brand: str = Field(min_length=1)
    model: str = Field(min_length=1)
    year: int = Field(gt=1980, lt=date.today().year)
    engine_capacity: int = Field(gt=800)
    gearbox: str = Field(min_length=1)
    fuel: str = Field(min_length=1)
    doors: int = Field(gt=2, lt=6)
    seats: int = Field(gt=3, lt=10)
    price: int = Field(gt=1)
    ac: bool = Field()
    abs: bool = Field()
