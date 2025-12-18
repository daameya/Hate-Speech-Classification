from hatespeech.logger import logging
from hatespeech.exception import CustomException
import sys
from hatespeech.configuration.gcloud_syncer import GCloudSync

obj = GCloudSync()
obj.sync_folder_from_gcloud("hate-speech2024", "dataset.zip", "download/dataset.zip")