#Define Database Models

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .permissions import Permissions  # Adjust the import as needed

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Directory(Base):
    __tablename__ = 'directories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('directories.id'))

    sub_directories = relationship('Directory', back_populates='parent')
    parent = relationship('Directory', remote_side=[id])

class File(Base):
    __tablename__ = 'files'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    group_id = Column(Integer, ForeignKey('groups.id'))
    permissions_id = Column(Integer, ForeignKey('permissions.id'))  # Assuming Permissions class

    user = relationship('User')
    group = relationship('Group')
    permissions = relationship('Permissions')
