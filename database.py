from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
databaseUrl = 'sqlite:///./emp.db'
engine = create_engine(databaseUrl,connect_args={"check_same_thread":False})
sessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)
base = declarative_base()
