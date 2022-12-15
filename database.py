# To Import
import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

# Constant

DATABASE_URL = "mysql+pymysql://root:Wini.h16b.@localhost:3306/hangman"

# Variables for database connection

Base = declarative_base()
engine = create_engine(DATABASE_URL)
LocalSession = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Database model

class Quests(BaseModel):
  ID: int
  Hint: str
  Answer: str
  AnswerLenght: int