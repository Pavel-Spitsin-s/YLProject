import sqlalchemy
from ..db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'viewers'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    session_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
