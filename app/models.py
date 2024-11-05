
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .connection import Base
from datetime import datetime

class Status(Base):
    __tablename__ = 'status'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    status = Column(Boolean, nullable=False)
    timestamp = Column(DateTime(timezone=True), default=datetime.utcnow)
