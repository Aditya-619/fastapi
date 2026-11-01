from fastapi import FastAPI, HTTPException, Path
import json

app = FastAPI()

@app.get('/')
def checkStatus():
    return {
        "status": "OK"
    }

def loadData():
    with open("data.json") as file:
        return json.load(file)

@app.get("/get-data")
def getData():
    return loadData()


@app.get("/get-data/{id}")
def getDataById(id: str = Path(...)):
    data = loadData()
    if id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"data not found"
        )
    return data[id]

@app.get("/filter")
def getFilteredData(course: str = None):

    data = loadData()
    if course is None:
        return data
    
    result = {}
    for id, info in data.items():
        if info["course"].lower() == course.lower():
            result[id] = info

    return result
    