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


def _add():
    c1 = CourtInfo('Taro', 'cray')
    c2 = CourtInfo('Hanako', 'omni')
    from database import db_session
    db_session.add(c1)
    db_session.add(c2)
    db_session.commit()

# _add()