import os
import sys
import pandas as pd

from hatespeech.logger import logging
from hatespeech.exception import CustomException
from hatespeech.constants import (
    IMBALANCED_DATA_COLUMNS,
    RAW_DATA_COLUMNS,
    ZIP_FILE_NAME
)
from hatespeech.entity.config_entity import DataValidationConfig
from hatespeech.entity.artifact_entity import DataValidationArtifacts, DataIngestionArtifacts

class DataValidation:
    def __init__(self,
        data_validation_config: DataValidationConfig,
        data_ingestion_artifacts: DataIngestionArtifacts):

        self.config = data_validation_config
        self.ingestion_artifacts = data_ingestion_artifacts
        os.makedirs(self.config.DATA_VALIDATION_ARTIFACTS_DIR, exist_ok=True)

    def _write_report(self, message: str):
        with open(self.config.VALIDATION_REPORT_PATH, "a") as f:
            f.write(message + "\n")

    
    def validate_files_exist(self) -> bool:
        logging.info("Validating required files existence")

        zip_path = os.path.join(
            os.path.dirname(self.ingestion_artifacts.imbalance_data_file_path),
            ZIP_FILE_NAME
        )
        
        files_exist = True

        for path in [
            zip_path,
            self.ingestion_artifacts.imbalance_data_file_path,
            self.ingestion_artifacts.raw_data_file_path
        ]:
            if not os.path.exists(path):
                self._write_report(f"[FAIL] File missing: {path}")
                files_exist = False
            else:
                self._write_report(f"[PASS] File exists: {path}")
            
        return files_exist
    

    def validate_csv(self, file_path: str, required_columns: list) -> bool:
        logging.info(f"Validating CSV: {file_path}")

        df = pd.read_csv(file_path)

        if df.empty:
            self._write_report(f"[FAIL] {file_path} is empty")
            return False
        
        missing_cols = set(required_columns) - set(df.columns)
        if missing_cols:
            self._write_report(
                f"[FAIL] Missing columns in {file_path}: {missing_cols}"
            )
            return False
        
        if df.isnull().sum().sum() > 0:
            self._write_report(
                f"[FAIL] Null Values found in {file_path}"
            )
            return False
        
        self._write_report(f"[PASS] CSV validated successfully: {file_path}")
        return True
    

    def initiate_data_validation(self) -> DataValidationArtifacts:
        logging.info("Entered initiate_data_validation method")

        try:
            validation_status = True

            if not self.validate_files_exist():
                validation_status = False

            if not self.validate_csv(
                self.ingestion_artifacts.imbalance_data_file_path,
                IMBALANCED_DATA_COLUMNS
            ):
                validation_status = False

            if not self.validate_csv(
                self.ingestion_artifacts.raw_data_file_path,
                RAW_DATA_COLUMNS
            ):
                validation_status = False

            self._write_report(
                f"\nFinal Validation Status: {validation_status}"
            )

            return DataValidationArtifacts(
                validation_status = validation_status,
                validation_report_path = self.config.VALIDATION_REPORT_PATH
            )
        
        except Exception as e:
            raise CustomException(e, sys) from e

            