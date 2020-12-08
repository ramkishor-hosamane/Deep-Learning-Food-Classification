from flask import Flask,render_template,Response,redirect,request
import cv2
from camera import VideoCamera
app = Flask(__name__)
#time.sleep(2)
from keras.models import load_model
import numpy as np
import os

PEOPLE_FOLDER = os.path.join('static', 'people_photo')

app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



is_stream = False
photo = None
def generate_frames(camera):
    global is_stream,photo
    while is_stream:
        data = camera.get_frame()

        frame = data[0]
        photo = frame
       
        #is_stream = False
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n'+ frame+ b'\r\n\r\n')
        
        #yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n'+ bytearray(encodedImage)+ b'\r\n')


@app.route("/")
def index():
    global is_stream
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
    return render_template("home.html",is_stream=is_stream,user_image = full_filename)

@app.route("/find")
def find():
    global is_stream

    img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'fruit.jpg')

    try:
        img = cv2.imread(img_path)
        model = load_model('newmodel.h5')
        shape = (100,100)
        img = cv2.resize(img,shape)
        predict = model.predict(np.array([img]))
        output = { 0:'apple',1:'banana',2:'orange'}
        result = output[np.argmax(predict)]
    except:
        result = "Not possible"
        print(result)
    return render_template("recognize.html",test_image = img_path,result=result)

    
@app.route("/ask")
def ask():
    global is_stream
    print("when asked",is_stream)
    is_stream = not is_stream


    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
    return render_template("home.html",is_stream=is_stream,user_image = full_filename)

@app.route("/video")
def video():
    return Response(generate_frames(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route("/local_photo", methods=['GET', 'POST'])
def local_photo():
    if request.method == 'POST':
        if 'uploaded_local_photo' not in request.files:
            print("No photos")
        uploaded_local_photo = request.files['uploaded_local_photo']
        print(uploaded_local_photo.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'fruit.jpg')
        print(path)

        uploaded_local_photo.save(path)
    return redirect("find")



if __name__ == "__main__":
    app.run(debug=True)