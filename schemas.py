from pydantic import BaseModel

class Quests(BaseModel):
  id: int
  hint: str
  answer: str
  answer_lenght: int

  class Config:
    orm_mode = True