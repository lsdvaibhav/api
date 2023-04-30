Using FastAPI with multiple use cases : 

-------------------- Upload file start -----------------------------
```
from fastapi import FastAPI, File, UploadFile
import shutil
```

1. Upload a single file to aws-S3-bucket via fastapi
```
@app.post("/upload-image-file")
async def image(image: UploadFile = File(...)):
    # save image to any folder or S3 bucket
    return {"filename": image.filename}
```
2. Upload a single file to local server
```
@app.post("/upload-image-file-to-server")
async def image(image: UploadFile = File(...)):
    
    # save to local server
    with open("path/destination.png", "wb") as buffer:
    	shutil.copyfileobj(image.file, buffer)

    return {"saved-filename": image.filename}
```
3. Upload a multiple files 
```
# save multiple files from requests
from typing import List
@app.post("/upload-mulitple-image-file-to-server")
async def image(images: List[UploadFile] = File(...)):
	for image in images:
    	with open(image.filename, "wb") as buffer:
        	shutil.copyfileobj(image.file, buffer)

    return {"saved-filenames": [i.filename for i in images]}
```
Let’s recap what we have learned today.

We started off with a simple problem statement explaining the lack of wrapper function in FastAPI to save uploaded files.

Next, we explored in-depth on the fundamental concept behind UploadFile and how to use it inside FastAPI server.

We have also implemented a simple file saving functionality using the built-in shutil.copyfileobj method. Besides, we have also tried extending our server to handle multiple files upload.

-------------------- Upload file ends -----------------------------
