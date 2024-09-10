from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from config import db_config
from handlers import start
from .models import Chanels, Base, User, Admin

engine = create_engine(db_config.db_path)
Base.metadata.create_all(engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)


def create_user(user_id: int, username: str = None, checkadmin: bool=False):
    db = SessionLocal()
    try:
        new_user = User(
            username=username,
            is_admin=checkadmin,
            user_id=user_id
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        return None

    finally:
        db.close()


def get_admin(user_id: int):
    db = SessionLocal()
    try:
        return db.query(Admin).filter(Admin.user_id ==user_id).first()
    except IntegrityError:
        db.rollback()

        raise e
    finally:
        pass


def get_all_users():
    db = SessionLocal()

    try:
        return db.query(User).all()
    finally:
        db.close()
