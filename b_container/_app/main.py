import warnings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from _app.api.routes import router as api_router
from _app.core.logging import setup_logging

# Ignorar advertencias
warnings.filterwarnings("ignore")

# Configurar el logger
setup_logging()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include the API router
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI ML Prediction Service!"}