import sqlalchemy
from .db_session import SqlAlchemyBase


class Session(SqlAlchemyBase):
    __tablename__ = 'session'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    date = sqlalchemy.Column(sqlalchemy.Date,
                              index=True, nullable=True)
    time = sqlalchemy.Column(sqlalchemy.Time,
                             index=True, nullable=True)
    cancel_code = sqlalchemy.Column(sqlalchemy.String)
    film_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)