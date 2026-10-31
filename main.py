from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def checkStatus():
    return {
        "status": "OK"
    }