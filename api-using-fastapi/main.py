# import the FastAPI class fastapi library
from fastapi import FastAPI 

# Create an application server using fastapi uvicorn server
app = FastAPI()

# root path for your first api
@app.get("/")
async def root():

	# return a sample json as a response
    return {"message": "Hello World"}