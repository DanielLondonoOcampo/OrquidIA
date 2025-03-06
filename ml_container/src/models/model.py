import numpy as np
import logging
from sklearn.ensemble import ExtraTreesClassifier
from src.data.data_loader import load_data, preprocess_data
# from src.data.data_transformation import transform_data
# from src.features.feature_engineering import create_features, select_features

# Configure logger
logger = logging.getLogger(__name__)
np.random.seed(37)

class ETC:
    def __init__(self):
        self.data = self.load_and_preprocess_data()
        self.final_model = self.model_training()

    def load_and_preprocess_data(self):
        """Load and preprocess data."""
        try:
            # Load data
            data = load_data("data/modified/MM_dataset_norm.csv")
            # Preprocess data
            data = preprocess_data(data)
            # Create features
            # data = create_features(data)
            # Split features and target variable
            X = data.drop(columns=["class"])
            y = data["class"]
            # Transform features
            # X_transformed = transform_data(X)
            logger.info("Data loaded and preprocessed successfully.")
            return X, y
        
        except Exception as e:
            logger.error("Error during data loading and preprocessing: %s", e)
            raise

    def model_training(self):
        """Train the Extra Trees Classifier model."""
        try:
            max_depth = 10
            criterion = "gini"
            et = ExtraTreesClassifier(max_depth=max_depth, criterion=criterion, random_state=40)
            
            # Fit the model using the transformed features and target variable
            final_model = et.fit(self.data[0], self.data[1].values.ravel())
            logger.info("Model training completed successfully.")
            return final_model
        
        except Exception as e:
            logger.error("Error during model training: %s", e)
            raise

    def predictT(self, input_data):
        """Make predictions using the trained model."""
        try:
            predictions = self.final_model.predict(input_data)
            return predictions
        
        except Exception as e:
            logger.error("Error during prediction: %s", e)
            raise