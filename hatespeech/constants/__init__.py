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