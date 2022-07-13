from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base


class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    year_born = Column(Integer)
    phone_number = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String, nullable=True)

    cars = relationship('Cars', back_populates='user')
    reviews = relationship('Reviews', back_populates='author')


class Cars(Base):

    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String)
    model = Column(String)
    year = Column(Integer)
    engine_capacity = Column(Integer)
    gearbox = Column(String)
    fuel = Column(String)
    doors = Column(Integer)
    seats = Column(Integer)
    price = Column(Integer)
    ac = Column(Boolean)
    abs = Column(Boolean)
    user_rented_id = Column(Integer, ForeignKey('users.id'), nullable=True)

    user = relationship('Users', back_populates='cars')


class Reviews(Base):

    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    rating = Column(Integer)
    author_id = Column(Integer, ForeignKey('users.id'))

    author = relationship('Users', back_populates='reviews')