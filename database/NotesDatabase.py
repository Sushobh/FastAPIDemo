from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class NotesDatabase:
    def __init__(self, username, password, host, port, database):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.engine = None
        self.Session = None

    def connect(self):
        conn_str = f'postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}'
        self.engine = create_engine(conn_str)
        self.Session = sessionmaker(bind=self.engine)

    def disconnect(self):
        self.engine.dispose()
