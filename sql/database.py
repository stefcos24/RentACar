import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost/RENTACAR_2022"
#SQLALCHEMY_DATABASE_URL = "postgresql://bkhnvfyyirizsy:8e2274369793c421bf8511ce08afa2f4fe7a78736f47f5933b93c4225d76f64c@ec2-3-219-229-143.compute-1.amazonaws.com:5432/db8laok9l6939i"
SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')

if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

