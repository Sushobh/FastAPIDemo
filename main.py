from typing import Union

from dotenv import load_dotenv
from fastapi import FastAPI

from sqlalchemy import create_engine, inspect

from controllers.NotesController import NotesController
from database.NotesDatabase import NotesDatabase
from database.NotesRepo import NotesRepo
from requestbodies.Bodies import NoteBody
import os


load_dotenv()


notes_db = NotesDatabase(username=os.environ['POSTGRES_USER'], password=os.environ['POSTGRES_PASSWORD'],
                         host=os.environ['POSTGRES_HOST'], port=os.environ['POSTGRES_PORT'],
                         database=os.environ['NOTES_DATABASE_NAME'])
notes_db.connect()
notes_repo = NotesRepo(db=notes_db)
notes_controller = NotesController(notes_repo=notes_repo)

app = FastAPI()


# Define the FastAPI endpoint
@app.post("/notes/")
def create_note(note: NoteBody):
    notes_controller.add_note(note)

    return {"message": "Done bro"}


