# import the FastAPI class fastapi library
from fastapi import FastAPI, File, UploadFile

# Create an application server using fastapi uvicorn server
app = FastAPI()

# root path for your first api
@app.get("/")
async def root():
	# return a sample json as a response
    return {"message": "Hello World"}

# api version 0.1
# pip install python-multipart
@app.post("/upload-image-file")
async def image(image: UploadFile = File(...)):
    # save image to any folder or S3 bucket
    return {"filename": image.filename}

import shutil
@app.post("/upload-image-file-to-server")
async def image(image: UploadFile = File(...)):
    
    # save to local server
    with open("path/destination.png", "wb") as buffer:
    	shutil.copyfileobj(image.file, buffer)

    return {"saved-filename": image.filename}


# save multiple files from requests
from typing import List
@app.post("/upload-mulitple-image-file-to-server")
async def image(images: List[UploadFile] = File(...)):
	for image in images:
    	with open(image.filename, "wb") as buffer:
        	shutil.copyfileobj(image.file, buffer)

    return {"saved-filenames": [i.filename for i in images]}