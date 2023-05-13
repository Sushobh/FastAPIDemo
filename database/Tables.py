from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the Note class, which maps to the 'notes' table
class NoteRow(Base):
    __tablename__ = 'notes'

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    Content = Column(String)