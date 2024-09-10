from sqlalchemy import Column, Integer, String,BigInteger,Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    # username it can be null
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=True,unique=True)
    is_admin = Column(Boolean, default=False)
    user_id = Column(BigInteger, unique=True, nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username},  user_id={self.user_id})>"
    

class Chanels(Base):
    __tablename__ = "chanels"
    id = Column(Integer, primary_key=True)
    chanel_id = Column(Integer,nullable=True) # chanel id
    name = Column(String(32)) # chanel username
    username = Column(String(32),unique=True,nullable=True) # chanel username
    
    def __repr__(self) -> str:
        
        return f"<Chanel(id={self.id},chanel_id={self.chanel_id},username={self.username },name={self.name})"
    

class Admin(Base):
   __tablename__ = "chanelsqeqwew"
   id  = Column(Integer,primary_key=True)
   user_id = Column(BigInteger,unique=True)
   
