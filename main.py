from functions.standard_deviation import standard_deviation
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel

class DataModel(BaseModel):
    data: list[float]

app = FastAPI()
app.mount("/static", StaticFiles(directory="./static"), name="static")

# Add async back if we need that 
@app.get("/")
def root():
    #return FileResponse(os.path.join(os.path.dirname(__file__), "../static/index.html")) # Run this if you get fucky behaviour
    #return FileResponse(os.path.join("static", "index.html"))
    return FileResponse("static/index.html")

@app.post("/calculate_standard_deviation")
def calc_std(request: DataModel):

    if not request.data:
        raise HTTPException(status_code=400, detail="Data list cannot be empty")
    
    res = standard_deviation(request.data)

    return {"standard_deviation" : res}

if __name__ == "__main__":
    root()