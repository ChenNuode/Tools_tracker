from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///database.db", connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)

Base = declarative_base()
