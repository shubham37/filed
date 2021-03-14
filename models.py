from datetime import  datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from database import Base


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(100), index=True, nullable=False)
    duration = Column(Integer, nullable=False, default=0)
    uploaded_time = Column(DateTime, nullable=False, default=datetime.now())


class Podcast(Base):
    __tablename__ = "podcasts"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(100), index=True, nullable=False)
    duration = Column(Integer, nullable=False, default=0)
    uploaded_time = Column(DateTime, nullable=False, default=datetime.now())
    host = Column(String(100), nullable=False)
    participants = Column(ARRAY(String(100)), nullable=True)


class Audiobook(Base):
    __tablename__ = "audiobooks"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    title = Column(String(100), index=True, nullable=False)
    duration = Column(Integer, nullable=False, default=0)
    uploaded_time = Column(DateTime, nullable=False, default=datetime.now())
    author = Column(String(100), nullable=False)
    narrator = Column(String(100), nullable=False)


