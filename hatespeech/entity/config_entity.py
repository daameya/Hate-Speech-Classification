from dataclasses import dataclass
import os
from hatespeech.constants import *

@dataclass
class DataIngestionConfig:
    def __init__(self):
        # Dataset Source
        self.SOURCE_URL: str = SOURCE_URL
        self.ZIP_FILE_NAME: str = ZIP_FILE_NAME

        # Base ingestion directory
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(
            os.getcwd(),
            ARTIFACTS_DIR,
            DATA_INGESTION_ARTIFACTS_DIR
        )

        # Data paths
        self.DATA_ARTIFACTS_DIR: str = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            DATA_INGESTION_IMBALANCE_DATA_DIR
        )

        self.NEW_DATA_ARTIFACTS_DIR: str = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            DATA_INGESTION_RAW_DATA_DIR
        )

        # ZIP paths
        self.ZIP_FILE_DIR: str = self.DATA_INGESTION_ARTIFACTS_DIR
        self.ZIP_FILE_PATH: str = os.path.join(
            self.DATA_INGESTION_ARTIFACTS_DIR,
            self.ZIP_FILE_NAME
        )


@dataclass
class DataValidationConfig:
    def __init__(self):
        self.DATA_VALIDATION_ARTIFACTS_DIR: str = os.path.join(
            os.getcwd(),
            ARTIFACTS_DIR,
            DATA_VALIDATION_ARTIFACTS_DIR
        )

        self.VALIDATION_REPORT_PATH: str = os.path.join(
            self.DATA_VALIDATION_ARTIFACTS_DIR,
            DATA_VALIDATION_REPORT_FILE
        )