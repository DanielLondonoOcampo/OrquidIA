import warnings
import pandas as pd
import logging
from fastapi import FastAPI, HTTPException
from src.api.schemas import PredictionResponse, InputData
from src.models.model import ETC

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

warnings.filterwarnings("ignore")

app = FastAPI()

# Initialize the ML model (this could also be done in a more sophisticated way)
etc = ETC()

@app.post("/predict", response_model=PredictionResponse)
def predict(data: InputData):
    try:
        logging.debug(f"Input data is {data}")
        
        # Convert input data to DataFrame for prediction
        input_data = pd.DataFrame({
            "anemia": [data.anemia],
            "creat": [data.creat],
            "prot_24": [data.prot_24],
            "ig": [data.ig],
            "chain": [data.chain],
            "ldh": [data.ldh],
            "fe": [data.fe],
        })

        # Perform prediction using the trained model
        prediction = etc.predictT(input_data)

        # Return the prediction as a JSON response
        logging.debug(f"Sending data to ML model API: {input_data}")
        return PredictionResponse(predicted_class=str(int(prediction[0])))
    
    except Exception as e:
        logging.debug("Data is %s", data)
        logging.exception("Error during prediction: %s", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
