Use case : 

Knowing how to integrate machine learning models into usable applications is an important skill for data scientists.
How you can deploy a spam detection model by building a REST API with FastAPI and running the API in a Docker container.

## Training a Spam Detection Model

Dataset link : 
``` http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/ ```
save the data file as spam_data.csv to data folder

Use ```train.py``` to train and save the spam-classifier model to artifacts folder

## FastAPI for Saved ML Model
Used the saved model from artifact folder to serve the classifier as api (FastAPI) ```main.py```.

