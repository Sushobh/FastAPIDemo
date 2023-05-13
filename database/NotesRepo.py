from database.Tables import NoteRow


class NotesRepo:
    def __init__(self, db):
        self.db = db

    def add_note_to_db(self, name, content):

        session = self.db.Session()
        new_note = NoteRow(Name=name, Content=content)
        session.add(new_note)
        session.commit()
        session.close()

    def get_notes_from_db(self):
        session = self.db.Session()
        notes = session.query(NotesRepo).all()
        session.close()
        return notes