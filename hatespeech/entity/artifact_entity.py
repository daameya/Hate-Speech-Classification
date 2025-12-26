from dataclasses import dataclass

# Data Ingestion artifacts

@dataclass
class DataIngestionArtifacts:
    imbalance_data_file_path: str
    raw_data_file_path: str


@dataclass
class DataValidationArtifacts:
    validation_report_path: str
    validation_status: bool