from models.postgresql.settings.base import Base
from sqlalchemy import Column, Integer, String

class Course(Base):
    __tablename__ = 'course'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    title: str = Column(String(100))
    classes: int = Column(Integer)
    hours: int = Column(Integer)
