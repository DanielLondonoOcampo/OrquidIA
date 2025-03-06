import logging
from fastapi import APIRouter, HTTPException
import httpx
from _app.api.schemas import InputData, PredictionResponse

router = APIRouter()

# Define the URL of the ML model API
ML_MODEL_API_URL = "http://m_learning:5000/predict"

@router.post("/submit", response_model=PredictionResponse)
async def submit(data: InputData):
    try:
        logging.debug(f"Input data is {data}")

        # Prepare data for sending to the ML model API as a JSON object
        json_data = {
            "anemia": data.anemia,
            "creat": data.creat,
            "prot_24": data.prot_24,
            "ig": data.ig,
            "chain": data.chain,
            "ldh": data.ldh,
            "fe": data.fe,
        }

        logging.debug(f"JSON payload sent to ML model API: {json_data}")

        # Send POST request to the ML model API with JSON data
        async with httpx.AsyncClient() as client:
            response = await client.post(ML_MODEL_API_URL, json=json_data, timeout = 20)
        
        # Check if the request was successful
        response.raise_for_status()  # Raise an error for bad responses
        
        # Return the prediction received from the ML model API
        prediction_result = response.json()
        return PredictionResponse(predicted_class=prediction_result["predicted_class"])
    
    except httpx.HTTPStatusError as http_error:
        logging.error(f"HTTP error occurred: {http_error.response.status_code} - {http_error.response.text}")
        raise HTTPException(status_code=http_error.response.status_code, detail="Error from ML model API")
    
    except Exception as e:
        logging.debug(f"Data is {json_data}")
        logging.exception(f"Error during data submission: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")