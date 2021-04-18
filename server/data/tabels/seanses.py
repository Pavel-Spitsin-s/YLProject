
import sqlalchemy
from ..db_session import SqlAlchemyBase


class Seanse(SqlAlchemyBase):
    __tablename__ = 'session'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    date = sqlalchemy.Column(sqlalchemy.Date,
                             index=True, nullable=False)
    time = sqlalchemy.Column(sqlalchemy.Time,
                             index=True, nullable=False)
    cost = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    room_name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    sides_left = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)