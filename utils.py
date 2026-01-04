import os
import sys
from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")

def read_sql_data():
    logging.info("Establishing database connection.")
    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        df = pd.read_sql_query("SELECT * FROM sales", mydb)
        logging.info("Database connection established.")
        print(df.head())
        return df
    except Exception as e:
        raise CustomException(e, sys)