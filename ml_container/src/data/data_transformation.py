# src/data/data_transformation.py

import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import logging

# Configure logger
logger = logging.getLogger(__name__)

def create_transformation_pipeline() -> Pipeline:
    numerical_features = ["anemia", "creat", "prot_24", "chain", "ldh", "fe"]
    categorical_features = ["ig"] 

    # Create transformers
    numerical_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder()

    # Create a preprocessing pipeline
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numerical_transformer, numerical_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    # Create and return the full pipeline
    pipeline = Pipeline(steps=[("preprocessor", preprocessor)])
    
    logger.info("Transformation pipeline created.")
    return pipeline

def transform_data(X: pd.DataFrame) -> pd.DataFrame:
    """Transform the feature set by applying the transformation pipeline."""
    try:
        # Create the transformation pipeline
        pipeline = create_transformation_pipeline()

        # Fit and transform the data
        X_transformed = pipeline.fit_transform(X)
        
        logger.info("Data transformation completed.")
        return pd.DataFrame(X_transformed)
    
    except Exception as e:
        logger.error("Error during data transformation: %s", e)
        raise