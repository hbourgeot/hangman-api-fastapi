# To Import
import pymysql
from sqlalchemy import create_engine, Column, Integer, String
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

class Quests(Base):
  __tablename__ = "quests"
  id = Column(Integer,primary_key=True)
  hint = Column(String(250))
  answer = Column(String(100))
  answer_lenght = Column(Integer)
  def __init__(self, id, hint, answer, answer_lenght):
    self.id=id
    self.hint=hint
    self.answer=answer
    self.answer_lenght=answer_lenght