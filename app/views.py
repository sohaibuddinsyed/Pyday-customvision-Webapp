# views.py

from flask import render_template
from msrest.authentication import ApiKeyCredentials
import time
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

from app import app

@app.route('/', methods=['GET','POST'])
def home():
    
    return render_template("home.html")


prediction_key = "21dcf849cf844333a0c1f45f6e5937aa"
prediction_resource_id = "/subscriptions/4199da6c-8f1e-4bfb-a8c1-62ba5bc76d73/resourceGroups/AzurePy/providers/Microsoft.CognitiveServices/accounts/TestCVP-Prediction"


@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        # # Now there is a trained endpoint that can be used to make a prediction
        # prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        # predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

        # with open(base_image_url + "withmask/testImg.jpg", "rb") as image_contents:
        #     results = predictor.classify_image(
        #     project.id, publish_iteration_name, image_contents.read())

        # # Display the results.
        # for prediction in results.predictions:
        #     print("\t" + prediction.tag_name +
        #           ": {0:.2f}%".format(prediction.probability * 100))
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)  


@app.route('/demo')
def demo():
    return render_template("demo.html")