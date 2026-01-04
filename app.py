from src.MLPROJECT.logger import logging
from src.MLPROJECT.exception import CustomException
import sys
from src.MLPROJECT.components.data_ingestion import DataIngestion
from src.MLPROJECT.components.data_ingestion import DataIngestionConfig
if __name__ == "__main__":
    logging.info("Starting the MLPROJECT application.")

    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Train data path: {train_data_path}")
        logging.info(f"Test data path: {test_data_path}")
    except Exception as e:
        logging.info("An exception occurred.")
        raise CustomException(e, sys)

