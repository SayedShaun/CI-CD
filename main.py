from typing import List
import fastapi
from pydantic import BaseModel
import pickle
import numpy as np

model = pickle.load(open('Saved Model/iris_model.pkl', 'rb'))
app = fastapi.FastAPI()

class Input(BaseModel):
    inputs: List[List[float]]

@app.post('/predict')
def predict(data: Input):
    inputs = np.array(data.inputs)
    prediction = model.predict(inputs)
    return {'prediction': prediction.tolist()}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)