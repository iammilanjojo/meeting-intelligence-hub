from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Transcript(Base):
    __tablename__ = "transcripts"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_type = Column(String)
    upload_time = Column(DateTime, default=datetime.utcnow)