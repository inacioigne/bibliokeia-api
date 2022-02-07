from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, LargeBinary, ForeignKey
#from sqlalchemy.types import JSON
from sqlalchemy.dialects.mysql import YEAR, JSON
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base() 

class Authorship(Base):
    __tablename__ = 'authorship'
    id = Column(Integer, primary_key=True)
    authority_id = Column(Integer, ForeignKey('authority.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    relation = Column(String(length=100))
    publicationyear = Column(YEAR)
    #relationship
    authority = relationship("Authority", back_populates="authorship")
    item = relationship("Item", back_populates="authorship")

    def __repr__(self):
        return self.relation
    
class Item_Subject(Base):
    __tablename__ = 'item_subject'
    id = Column(Integer, primary_key=True)
    authority_id = Column(Integer, ForeignKey('authority.id'))
    subject_id = Column(Integer, ForeignKey('subject.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    relation = Column(String(length=100))
    #relationship
    subject = relationship("Subject", back_populates="item_subject")
    authority = relationship("Authority", back_populates="item_subject")
    item = relationship("Item", back_populates="item_subject")

    def __repr__(self):
        return self.relation

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=255))
    marc = Column(JSON)
    #format = Column(String(length=100), default='marc_utf8')
    #schema = Column(String(length=100), default='marc21')
    #marc_record = Column(LargeBinary)
    created_at = Column(Date, default=datetime.now())

    #relationship
    authorship = relationship("Authorship", back_populates="item")
    item_subject = relationship("Item_Subject", back_populates="item")

    def __repr__(self):
        return self.title

class Authority(Base):
    __tablename__ = 'authority'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    format = Column(String(length=100), default='marcxml')
    schema = Column(String(length=100), default='marc21')
    marc_record = Column(LargeBinary)
    created_at = Column(Date, default=datetime.now())

    authorship = relationship("Authorship", back_populates="authority")
    item_subject = relationship("Item_Subject", back_populates="authority")

    def __repr__(self):
        return self.name

class Subject(Base):
    __tablename__ = 'subject'
    id = Column(Integer, primary_key=True)
    name = Column(String(length=255))
    tag = Column(String(length=5))
    format = Column(String(length=100), default='marcxml')
    schema = Column(String(length=100), default='marc21')
    marc_record = Column(LargeBinary)
    created_at = Column(Date, default=datetime.now())

    item_subject = relationship("Item_Subject", back_populates="subject")

    def __repr__(self):
        return self.name
