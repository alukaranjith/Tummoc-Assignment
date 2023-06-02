from fastapi import FastAPI
from pydantic import BaseModel
import math

app = FastAPI()

class Coordinates(BaseModel):
    lat1: float
    lon1: float
    lat2: float
    lon2: float

@app.post("/distance")
def calculate_distance(coords: Coordinates):
    x_diff = coords.lat2 - coords.lat1
    y_diff = coords.lon2 - coords.lon1
    distance = math.sqrt(x_diff ** 2 + y_diff ** 2)
    return {"distance": distance}
