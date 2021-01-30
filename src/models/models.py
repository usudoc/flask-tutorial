from sqlalchemy import Column, Integer, String, Text, DateTime
from models.database import Base
from datetime import datetime


class CourtInfo(Base):
    __tablename__ = 'courtinfo'
    # __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True)
    type = Column(String(128), unique=True)
    date = Column(DateTime, default=datetime.now())

    def __init__(self, name=None, type=None, date=None):
        self.name = name
        self.type = type
        self.date = date

    def __repr__(self):
        return '<Name %r>' % (self.name)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(128), unique=True)
    hashed_password = Column(String(128))

    def __init__(self, user_name=None, hashed_password=None):
        self.user_name = user_name
        self.hashed_password = hashed_password

    def __repr__(self):
        return '<Name %r>' % (self.user_name)
