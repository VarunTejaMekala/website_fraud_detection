import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for training pipeline
"""

TARGET_COLUMN: str ="Result"
PIPELINE_NAME: str ="NetwrokSecurity"
ARTIFACT_DIR: str ="Artifacts"
FILE_NAME: str ="phisingData.csv"

TRAIN_FILE_NAME: str ="train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH: str =os.path.join("data_schema","schema.yaml")

SAVED_MODEL_DIR: str =os.path.join("saved_model")
MODEL_FILE_NAME: str="model.pkl"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME: str ="NetworkData"
DATA_INGESTION_DATABASE_NAME: str ="varuntejamekala123_db_user"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str="feature_store"
DATA_INGESTION_INGESTED_DIR: str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float =0.2