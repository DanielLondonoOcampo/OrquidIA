import pandas as pd
import logging

logger = logging.getLogger(__name__)

def create_features(data: pd.DataFrame) -> pd.DataFrame:
    try:
        data['anemia_ratio'] = data['anemia'] / data['fe']
        
        # Log the creation of new features
        logger.info("New features created successfully.")
        
        return data
    
    except Exception as e:
        logger.error("Error during feature creation: %s", e)
        raise

def select_features(X: pd.DataFrame, y: pd.Series) -> pd.DataFrame:
    """Select relevant features for modeling."""
    try:
        # For simplicity, we are returning all features in this example.
        # You can implement feature selection logic here (e.g., using correlation, model importance).
        
        logger.info("Feature selection completed.")
        return X  # Modify this to return selected features if needed
    
    except Exception as e:
        logger.error("Error during feature selection: %s", e)
        raise