# To import
from fastapi import FastAPI, Depends, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
import database, db_operations, schemas

# Database object
def get_database_session():
  db = database.LocalSession()
  try:
    yield db
  finally:
    db.close()

# New FastAPI app
app = FastAPI()

origins = [
  "http://127.0.0.1",
  "http://localhost"
]
app.add_middleware(
                   CORSMiddleware,
                   allow_origins=origins,
                   allow_methods=["POST","GET"]
                   )

# Routes
@app.get("/get/hangman/{quest_id}", response_model=schemas.Quests)
def get_hangman(quest_id: int, db: Session = Depends(get_database_session)):
  quest = db_operations.get_from_db(db, quest_id)
  if quest is None:
    raise HTTPException(status_code=404,detail="Quest not found.")
  return quest


@app.post("/new/hangman", response_model=schemas.Quests)
def new_hangman(quest: schemas.Quests, db: Session = Depends(get_database_session)):
  db_quest = db_operations.add(db, quest)
  if db_quest is None:
    raise HTTPException(status_code=400,detail="ID already registered, try another.")
  return db_quest