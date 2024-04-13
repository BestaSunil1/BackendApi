# models.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    emp_id = Column(String, nullable=False)
    emp_name = Column(String, nullable=False)
    mobile = Column(String, nullable=False)
    email = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    department = Column(String, nullable=False)
    role = Column(String, nullable=False)
