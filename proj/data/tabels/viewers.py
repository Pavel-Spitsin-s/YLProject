import sqlalchemy
from ..db_session import SqlAlchemyBase


class Viewer(SqlAlchemyBase):
    __tablename__ = 'viewers'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    cancel_code = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    session_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
