from flask import *
import os
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from app import app


prediction_key = "your-prediction key"
publish_iteration_name = "classifyModel"
ENDPOINT = "your-endpoint"
projectId = "your project id"
