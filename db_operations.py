from sqlalchemy.orm import Session
import database,schemas

def get_from_db(db: Session, quest_id:int):
  hangman = db.query(database.Quests).filter(database.Quests.id == quest_id).first()
  return hangman

def add(db: Session, quest: schemas.Quests):
  new_quest = database.Quests(quest.id,quest.hint,quest.answer,len(quest.answer))
  quest_exists = get_from_db(db, quest.id)
  if quest_exists: return None
  
  db.add(new_quest)
  db.commit()
  db.refresh(new_quest)
  return new_quest