# SQLAlchemy
from sqlalchemy import create_engine, text


def init_db(url):
    engine = create_engine(url, echo=True)

    with engine.connect() as db:
        with open("db/init.sql") as file:
            query = text(file.read())
            db.execute(query)

    return engine
