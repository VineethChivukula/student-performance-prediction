import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join(
        'artifacts', 'train.csv')  # Path to save the train data
    test_data_path: str = os.path.join(
        'artifacts', 'test.csv')  # Path to save the test data
    raw_data_path: str = os.path.join(
        'artifacts', 'data.csv')  # Path to save the raw data


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Initiating data ingestion")
        try:
            # Read the data from the specified file
            data = pd.read_csv("src\data\data.csv")
            logging.info("Data ingestion successful")
            os.makedirs(os.path.dirname(
                self.ingestion_config.train_data_path), exist_ok=True)  # Create the directory to save train data if it doesn't exist
            data.to_csv(self.ingestion_config.raw_data_path,
                        index=False, header=True)  # Save the raw data to the specified path
            logging.info("Data saved successfully")
            train_set, test_set = train_test_split(
                data, test_size=0.2, random_state=42)  # Split the data into train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path,
                             index=False, header=True)  # Save the train data to the specified path
            test_set.to_csv(self.ingestion_config.test_data_path,
                            index=False, header=True)  # Save the test data to the specified path
            logging.info("Data splitted successfully")
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)

        except Exception as e:
            logging.error("Data ingestion failed")
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
