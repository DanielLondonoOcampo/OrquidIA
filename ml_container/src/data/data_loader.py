# src/data/data_loader.py

import pandas as pd
import logging

# Configure logger
logger = logging.getLogger(__name__)

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        logger.info(f"Data loaded successfully from {file_path}.")
        return data
    except Exception as e:
        logger.error(f"Error loading data from {file_path}: {e}")
        raise

def preprocess_data(data: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data by selecting relevant columns and renaming them."""
    try:
        # Select relevant columns
        data = data[["anemia", "creat", "24h_prot", "Ig", "chain", "LDH", "FE", "class"]]
        data.rename(columns={
            "24h_prot": "prot_24",
            "Ig": "ig",
            "LDH": "ldh",
            "FE": "fe"
        }, inplace=True)
        data.reset_index(drop = True, inplace = True)
        logger.info("Data preprocessing completed.")
        return data
    except Exception as e:
        logger.error("Error during data preprocessing: %s", e)
        raise