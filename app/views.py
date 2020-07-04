# views.py

from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

prediction_key = "21dcf849cf844333a0c1f45f6e5937aa"
publish_iteration_name = "classifyModel"
ENDPOINT = "https://testcvp.cognitiveservices.azure.com/"
projectId = "dc248edb-8a7d-4314-90a7-0494403301a3"


from app import app

@app.route('/', methods=['GET','POST'])
def home():
    
    return render_template("home.html")


@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(os.path.join(app.root_path, "static","test.jpg")) 

        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

        with open(app.root_path + "/static/test.jpg", "rb") as image_contents:
            results = predictor.classify_image(
                projectId, publish_iteration_name, image_contents.read())
            result=""
            for prediction in results.predictions:
                result += "\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100)

        return render_template("success.html", result = result)  


@app.route('/demo')
def demo():
    return render_template("demo.html")