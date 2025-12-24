import os
import sys
import requests
from zipfile import ZipFile

from hatespeech.logger import logging
from hatespeech.exception import CustomException
from hatespeech.entity.config_entity import DataIngestionConfig
from hatespeech.entity.artifact_entity import DataIngestionArtifacts

class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

    def download_data_from_github(self) -> None:
        """
        Download dataset.zip from GitHub repository
        """
        try:
            logging.info(
                "Entered the download_data_from_github method of DataIngestion class"
            )

            os.makedirs(
                self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,
                exist_ok=True
            )

            response = requests.get(
                self.data_ingestion_config.SOURCE_URL,
                stream=True
            )
            response.raise_for_status()

            with open(self.data_ingestion_config.ZIP_FILE_PATH, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)

            logging.info(
                "Exited the downloaded_data_from_github method of DataIngestion class"
            )
        
        except Exception as e:
            raise CustomException(e, sys) from e

    def unzip_and_clean(self):
        """
        Extract dataset.zip
        """
        logging.info(
            "Entered the unzip_and_clean method of DataIngestion class"
        )

        try:
            with ZipFile(self.data_ingestion_config.ZIP_FILE_PATH, "r") as zip_ref:
                zip_ref.extractall(self.data_ingestion_config.ZIP_FILE_DIR)

            logging.info(
                "Exited the unzip_and_clean method of DataIngestion class"
            )

            return (
                self.data_ingestion_config.DATA_ARTIFACTS_DIR,
                self.data_ingestion_config.NEW_DATA_ARTIFACTS_DIR
            )
        
        except Exception as e:
            raise CustomException(e, sys) from e
        

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info(
            "Entered the initiate_data_ingestion method of DataIngestion class"
        )

        try:
            self.download_data_from_github()
            logging.info("Fetch the data from GitHub repository")

            imbalance_data_file_path, raw_data_file_path = self.unzip_and_clean()
            logging.info("Unzipped dataset successfully")

            data_ingestion_artifacts = DataIngestionArtifacts(
                imbalance_data_file_path=imbalance_data_file_path,
                raw_data_file_path=raw_data_file_path
            )

            logging.info(
                "Exited the initiate_data_ingestion method of DataIngestion class"
            )

            return data_ingestion_artifacts
        
        except Exception as e:
            raise CustomException(e, sys) from e

        

