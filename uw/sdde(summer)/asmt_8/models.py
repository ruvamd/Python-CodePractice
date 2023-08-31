from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    root_directory = relationship('Directory', uselist=False, back_populates='owner')

class Directory(Base):
    __tablename__ = 'directories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))
    owner = relationship('User', back_populates='root_directory')
    parent_id = Column(Integer, ForeignKey('directories.id'))
    parent = relationship('Directory', remote_side=[id])
    
    files = relationship('File', back_populates='directory')

class File(Base):
    __tablename__ = 'files'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    directory_id = Column(Integer, ForeignKey('directories.id'))
    directory = relationship('Directory', back_populates='files')

engine = create_engine('sqlite:///filesystem.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
