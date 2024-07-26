"""Database module"""

from sqlmodel import Session, SQLModel, create_engine

from src.config import SETTINGS, Settings


class Database:
    """Database class to interact with the db"""

    def __init__(self, config: Settings):
        self._engine = create_engine(f"sqlite:///{config.DB_URL}", echo=True)

    def create_db_and_tables(self):
        """
        Init the db engine
        """
        SQLModel.metadata.create_all(self._engine)

    def get_session(self):
        """Get database session"""

        with Session(self._engine) as session:
            return session
        self._engine.dispose()


DB = Database(config=SETTINGS)
