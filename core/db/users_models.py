from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)
    username = Column(String)
    email = Column(String)
    phonenumber = Column(String)
    password_1 = Column(String)
    password_2 = Column(String)


class UserLogin(Base):
    __tablename__ = 'user_logins'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="login")
    email = Column(String)
    phonenumber = Column(String)
    password = Column(String)
