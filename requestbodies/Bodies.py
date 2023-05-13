from pydantic import BaseModel


class NoteBody(BaseModel):
    name: str
    text: str