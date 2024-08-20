from typing import List
import fastapi
from pydantic import BaseModel
import pickle
import numpy as np

model = pickle.load(open('iris_model.pkl', 'rb'))
app = fastapi.FastAPI()

class Input(BaseModel):
    inputs: List[List[float]]

@app.post('/predict')
def predict(data: Input):
    prediction = model.predict(data.inputs)
    return {'prediction': prediction}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)