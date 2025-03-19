from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base
class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    last_seen_location = Column(String, nullable=False)
    date_missing = Column(DateTime, default=datetime.utcnow)
    photo_url = Column(String, nullable=False)  # Path to image
    status = Column(String, default="Missing")  # Missing, Found, Reunited
    reporter_id = Column(Integer, ForeignKey("users.id"))  # Link to user who reported

    reporter = relationship("User", back_populates="reported_children")
