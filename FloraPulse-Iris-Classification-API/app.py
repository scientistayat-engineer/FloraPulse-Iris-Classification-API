
import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field

# 1. Initialize production framework instance
app = FastAPI(
    title="FloraPulse - Iris Variant Inference Core",
    description="Automated biological classification engine exposing high-availability REST endpoints.",
    version="1.0.0"
)

# 2. Load the binary serialization layer safely
predictive_pipeline = joblib.load("iris_random_forest_model.pkl")
target_species_mapping = ["setosa", "versicolor", "virginica"]

# 3. Define robust data schema validation framework using Pydantic
class IrisInferenceSchema(BaseModel):
    sepal_length: float = Field(..., example=5.1, description="Length of the sepal in centimeters.")
    sepal_width: float = Field(..., example=3.5, description="Width of the sepal in centimeters.")
    petal_length: float = Field(..., example=1.4, description="Length of the petal in centimeters.")
    petal_width: float = Field(..., example=0.2, description="Width of the petal in centimeters.")

# 4. Endpoint 1: Health Diagnostic / Greetings Router Gateway
@app.get("/")
def system_health_handshake():
    return {
        "status": "online",
        "message": "Welcome to the Vanguard Systems Iris Species Classification API Gateway!"
    }

# 5. Endpoint 2: Automated Real-time Matrix Prediction
@app.post("/predict")
def route_live_inference(payload: IrisInferenceSchema):
    # Format structural input fields into standard numerical vector row
    feature_vector = np.array([[
        payload.sepal_length, 
        payload.sepal_width, 
        payload.petal_length, 
        payload.petal_width
    ]])
    
    # Execute class extraction inference via random forest algorithm state
    class_index_result = predictive_pipeline.predict(feature_vector)[0]
    resolved_species_string = target_species_mapping[class_index_result]
    
    return {
        "prediction": resolved_species_string
    }
