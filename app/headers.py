from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from app import app



prediction_key = "21dcf849cf844333a0c1f45f6e5937aa"
publish_iteration_name = "classifyModel"
ENDPOINT = "https://testcvp.cognitiveservices.azure.com/"
projectId = "dc248edb-8a7d-4314-90a7-0494403301a3"
# prediction_key = "your-prediction key"
# publish_iteration_name = "classifyModel"
# ENDPOINT = "your-endpoint"
# projectId = "your project id"
