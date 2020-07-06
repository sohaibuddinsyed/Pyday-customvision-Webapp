from .headers import *
import cv2

# PRevents the application from caching the inputs to the browser
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

# Aclass that defines,initializes and generates input from the device camera
class Camera(object):
  def __init__(self):
    self.cap = cv2.VideoCapture(0)

  def get_frame(self):
    ret, frame = self.cap.read()
    ret, jpg = cv2.imencode('.jpg', frame)
    return jpg.tobytes()
    
def gen(camera):
  while True:
    frame = camera.get_frame()
    yield (b'--frame\r\n'
      b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
  return Response(gen(Camera()),
  mimetype='multipart/x-mixed-replace;boundary=frame') 
 
@app.route('/', methods=['GET','POST'])
def home():
    return render_template("home.html")

def redirecting():
    return render_template("demo.html")

@app.route('/demo')
def demo():
    return render_template("demo.html")

# Route triggered whn the upload is successful
@app.route('/result', methods = ['POST'])  
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

        return render_template("result.html", result = result)  


# Route triggered whn the Live capture is successful
@app.route('/result-capture', methods = ['POST'])  
def success1():  
    if request.method == 'POST':  
        ret,img = cv2.VideoCapture(0).read()
        cv2.imwrite(os.path.join(app.root_path, "static","test1.jpg"),img)
        prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
        predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)

        with open(app.root_path + "/static/test1.jpg", "rb") as image_contents:
            results = predictor.classify_image(
                projectId, publish_iteration_name, image_contents.read())
            result=""
            for prediction in results.predictions:
                result += "\t" + prediction.tag_name + ": {0:.2f}%".format(prediction.probability * 100)

        return render_template("result-capture.html",result = result)  

