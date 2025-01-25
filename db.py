from decouple import config
from sqlalchemy import create_engine
import pandas as pd



username = config("USERNAME")
password = config("PASSWORD")
driver = config("DRIVER")
server = config("SERVER")
database = config("DATABASE")


connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"


engine =create_engine(connection_string)













   