# To import
from fastapi import FastAPI, Body, Request, Response
from fastapi.staticfiles import StaticFiles
import database

# Database object
def get_database_session():
  try:
    db = database.LocalSession()
    yield db
  finally:
    db.close()

# New FastAPI app
app = FastAPI()

# Static files
app.mount("/", StaticFiles(directory="static"), name="static")

# Routes
@app.get("/get/hangman")
def getHangman():
  return

@app.post("/new/hangman")
def newHangman(quests: database.Quests = Body(...)):
  return