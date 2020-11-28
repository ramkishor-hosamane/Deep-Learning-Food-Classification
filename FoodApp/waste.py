def gen_photo(camera):
    data = camera.get_frame()
    frame = data[0]
    print(frame)
    yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n'+ frame+ b'\r\n\r\n')

@app.route("/photo")
def photo():
    global is_stream,photo
    print("Returned")
    return Response(gen_photo(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')
                <!-- <img src="{{ url_for('ds') }}" alt=""> -->    
