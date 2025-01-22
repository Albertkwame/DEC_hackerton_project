from decouple import config
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy.orm import sessionmaker,scoped_session,declarative_base
from sqlalchemy import Column, BigInteger, DateTime, Integer, Text, func, Boolean, Float




username = config("USERNAME")
password = config("PASSWORD")
driver = config("DRIVER")
server = config("SERVER")
database = config("DATABASE")


connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"


engine =create_engine(connection_string)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
RestSession  = scoped_session(session)
 

BASE = declarative_base()

class RestCountry(BASE):
   __tablename__ = 'rest_countries'

   id = Column(BigInteger, primary_key=True, nullable=False)
   Country_name = Column(Text)
   Independent = Column(Text)
   United_Nation_members = Column(Text)
   startOfWeek= Column(Text)
   Official_country_name = Column(Text)
   Common_native_name = Column(Text)
   idd_root = Column(Text)
   idd_suffixes =  Column(Text)
   Capital = Column(Text)
   Region = Column(Text)
   Sub_region = Column(Text)
   Languages = Column(Text)
   Area = Column(Float) 
   Population = Column(Integer)
   Continents = Column(Text)
   Currency_code = Column(Text)
   Currency_name = Column(Text)
   Currency_symbol = Column(Text)

   