import sqlalchemy
from .db_session import SqlAlchemyBase


class Viewers(SqlAlchemyBase):
    __tablename__ = 'viewers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)
    cancel_code = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    film_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
