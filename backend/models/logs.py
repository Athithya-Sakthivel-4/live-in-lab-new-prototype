from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    event = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, nullable=True)
    details = Column(String, nullable=True)

