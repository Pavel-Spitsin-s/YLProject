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
                             index=True, nullable=True)
    room_name = sqlalchemy.Column(sqlalchemy.String, nullable=False, index=True)
    cancel_code = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    session_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
