import os

from datetime import datetime

#common constants
TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

ARTIFACTS_DIR = os.path.join("artifacts", TIMESTAMP)

ZIP_FILE_NAME = "dataset.zip"
SOURCE_URL = "https://github.com/daameya/datasets/raw/refs/heads/main/dataset.zip"

LABEL = "label"
TWEET = "tweet"

# Data ingestion constants
DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_IMBALANCE_DATA_DIR = "imbalanced_data.csv"
DATA_INGESTION_RAW_DATA_DIR = "raw_data.csv"

# Data validation constants
DATA_VALIDATION_ARTIFACTS_DIR = "DataValidationArtifacts"
DATA_VALIDATION_REPORT_FILE = "data_validation_report.txt"
IMBALANCED_DATA_COLUMNS = ["id", "label", "tweet"]
RAW_DATA_COLUMNS = [
    
    "count",
    "hate_speech",
    "offensive_language",
    "neither",
    "class",
    "tweet"
]