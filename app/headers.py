from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from app import app



prediction_key = "21dcf849cf844333a0c1f45f6e5937aa"
publish_iteration_name = "classifyModel"
ENDPOINT = "https://testcvp.cognitiveservices.azure.com/"
projectId = "e9d53526-fb02-4522-8c89-74d65fa3a624"
# prediction_key = "your-prediction key"
# publish_iteration_name = "classifyModel"
# ENDPOINT = "your-endpoint"
# projectId = "your project id"
