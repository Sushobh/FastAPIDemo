from pydantic import BaseModel


class NoteModel:
    id : int
    name: str
    text: str