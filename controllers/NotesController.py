# Define the NotesController class
from typing import List

from database import NotesRepo
from models.Notes import NoteModel
from requestbodies.Bodies import NoteBody


class NotesController:
    def __init__(self, notes_repo: NotesRepo):
        self.notes_repo = notes_repo

    def add_note(self, note: NoteBody):
        self.notes_repo.add_note_to_db(name=note.name, content=note.text)

    def get_notes(self) -> List[NoteModel]:
        notes = self.notes_repo.get_notes_from_db()
        return [NoteModel(name=note.name, text=note.text) for note in notes]