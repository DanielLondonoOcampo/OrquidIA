from pydantic import BaseModel

class InputData(BaseModel):
    anemia: int
    creat: float
    prot_24: int
    ig: int
    chain: int
    ldh: float
    fe: float

class PredictionResponse(BaseModel):
    predicted_class: str