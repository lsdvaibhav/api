# Use case : 

Knowing how to integrate machine learning models into usable applications is an important skill for data scientists.
How you can deploy a spam detection model by building a REST API with FastAPI and running the API in a Docker container.

## Training a Spam Detection Model

Dataset link : 
``` http://www.dt.fee.unicamp.br/~tiago/smsspamcollection/ ```
save the data file as spam_data.csv to data folder

Use ```train.py``` to train and save the spam-classifier model to artifacts folder
The code in train.py performs the following steps:

1. Reads the spam dataset.
2. Splits the spam dataset into training and testing sets.
3. Creates a text preprocessing and deep learning pipeline for spam classification.
4. Trains the model pipeline on the training set.
5. Evaluates the model pipeline on the testing set.
6. Saves the trained model pipeline.

## FastAPI for Saved ML Model
Used the saved model from artifact folder to serve the classifier as api (FastAPI) ```main.py```.

With FastAPI, we can define GET requests to retrieve the spam detection model’s predictions.

### Loading the Model and Defining Helper Functions

Before defining the GET request that invokes the spam detection model, we need to first load the model and define functions for preprocessing the text data and returning the model’s predictions.

```
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
The ```preprocessor``` function above removes emoticons and unwanted characters from the text input while the classify_message function calls the preprocessor function to clean a text message before using the spam detection model to generate predictions. The ```classify_message``` function returns a dictionary, which can conveniently be interpreted as a JSON response.

### Defining the Spam Detection GET Request

FastAPI makes it really easy to supply and read variables for GET requests. You can supply the inputs of a machine learning model to a GET request using query parameters or path variables.

Using Query Parameters

For a REST API, query parameters are part of the URL string and are prefixed by a “?”. For example, for the spam detection API we are creating, a GET request could look like this:

```127.0.0.1.8000/spam_detection_query/?message=’hello, please reply to this message’```

Notice how the message argument at the end is a query parameter. We can write a function that accepts a message as a query parameter and classifies it as ham or spam as demonstrated below.

```
@app.get('/spam_detection_query/')
async def detect_spam_query(message: str):
   return classify_message(model, message)
```
If we navigate to the localhost URL, we can test this code with a sample message and response ``` {'label': "Label", 'spam_probability': 0.999} ```

At this point, after writing less than 40 lines of code, we have a functioning REST API for spam detection.

We can also use this documentation page to test each of the GET commands as demonstrated in the GIF below:
<<<<<<< HEAD
![demo]('1_COUA-0NlTzOLQAdN-uCluA.gif')
=======
![demo](`r https://miro.medium.com/v2/resize:fit:720/1*XNIR-K4rRdGfLvAIxHj3aw.gif`)
>>>>>>> 7d683063164df1f9b50e2a8680b9aac60276df69
