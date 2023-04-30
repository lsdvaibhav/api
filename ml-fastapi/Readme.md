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

-------------------- request a ml model to classify based on Passed data file start -----------------------------

Use Case : We can deploy a spam detection model by building a REST API with FastAPI with get method.


The preprocessor function above removes emoticons and unwanted characters from the text input while the classify_message function calls the preprocessor function to clean a text message before using the spam detection model to generate predictions. The classify_message function returns a dictionary, which can conveniently be interpreted as a JSON response.
```
import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI

model = joblib.load('spam_classifier.joblib')
def preprocessor(text):
    text = re.sub('<[^>]*>', '', text) # Effectively removes HTML markup tags
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    return text
def classify_message(model, message):
    message = preprocessor(message)
    label = model.predict([message])[0]
    spam_prob = model.predict_proba([message])
    return {'label': label, 'spam_probability': spam_prob[0][1]}
```

FastAPI makes it really easy to supply and read variables for GET requests. You can supply the inputs of a machine learning model to a GET request using query parameters or path variables.

```
@app.get('/spam_detection_query/')
async def detect_spam_query(message: str):
   return classify_message(model, message)
```

test it - 
```
127.0.0.1.8000/spam_detection_query/hello, please reply to this message
```

-------------------- request a ml model to classify based on Passed data file ends -----------------------------