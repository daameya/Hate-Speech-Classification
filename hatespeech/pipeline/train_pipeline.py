import sys

from hatespeech.logger import logging
from hatespeech.exception import CustomException
from hatespeech.components.data_ingestion import DataIngestion
from hatespeech.components.data_validation import DataValidation
from hatespeech.entity.config_entity import (DataIngestionConfig, DataValidationConfig)
from hatespeech.entity.artifact_entity import (DataIngestionArtifacts, DataValidationArtifacts)

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()


    def start_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")
        try:
            logging.info("Starting data ingestion from GitHub repository")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifacts = data_ingestion.initiate_data_ingestion()
            logging.info("Successfully ingested data from GitHub repository")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifacts
        
        except Exception as e:
            raise CustomException(e, sys) from e
        
    
    def start_data_validation(self, data_ingestion_artifacts: DataIngestionArtifacts) -> DataValidationArtifacts:

        logging.info("Entered start_data_validation method of TrainPipeline class")
        try:
            data_validation_config = DataValidationConfig()

            data_validation = DataValidation(
                data_ingestion_artifacts = data_ingestion_artifacts,
                data_validation_config = data_validation_config
            )

            data_validation_artifacts = (
                data_validation.initiate_data_validation()
            )

            if not data_validation_artifacts.validation_status:
                raise Exception(
                    "Data Validation failed Check validation report."
                )
            
            logging.info("Exited start_data_validation method of TrainPipeline Class")

            return data_validation_artifacts

        except Exception as e:
            raise CustomException(e, sys) from e


    def run_pipeline(self):
        logging.info("Entered the run_pipeline method of TrainPipeline class")
        try:
            data_ingestion_artifacts = self.start_data_ingestion()
            data_validation_artifacts = self.start_data_validation(data_ingestion_artifacts)            

            logging.info("Exited the run_pipeline method of TrainPipline class")

        except Exception as e:
            raise CustomException(e, sys) from e