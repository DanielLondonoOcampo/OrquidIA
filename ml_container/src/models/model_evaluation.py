# src/models/model_evaluation.py

import logging
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd

# Configure logger
logger = logging.getLogger(__name__)

def evaluate_model(model, X_test: pd.DataFrame, y_test: pd.Series) -> dict:
    """Evaluate the model's performance on the test set."""
    try:
        # Make predictions on the test set
        predictions = model.predict(X_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, predictions)
        
        # Generate a classification report
        report = classification_report(y_test, predictions, output_dict=True)
        
        # Generate a confusion matrix
        cm = confusion_matrix(y_test, predictions)

        logger.info("Model evaluation completed successfully.")
        
        return {
            "accuracy": accuracy,
            "classification_report": report,
            "confusion_matrix": cm.tolist()  # Convert to list for better JSON serialization
        }
    
    except Exception as e:
        logger.error("Error during model evaluation: %s", e)
        raise