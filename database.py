from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = 'sqlite:///./product.db'

engine = create_engine(DB_URL,connect_args={'check_same_thread':False})

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)