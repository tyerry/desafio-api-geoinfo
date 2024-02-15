from sqlalchemy import Column, Integer, String
from database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    region = Column(Integer)
    population = Column(Integer)
    keyword = Column(String)
