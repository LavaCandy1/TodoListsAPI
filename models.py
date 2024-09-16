from sqlalchemy import String, Integer,Column, Boolean
from database import Base

class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key = True, index = True)
    todo_text = Column(String , index = True)
    # completed = Column(Boolean , default = False)

