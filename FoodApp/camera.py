import cv2
from imutils.video import WebcamVideoStream



class VideoCamera(object):
    def __init__(self):
        self.stream = WebcamVideoStream(src=0).start()

    def __del__(self):
        self.stream.stop()

    def get_frame(self):
        x,y = 50,50
        w,h = 150,150
        image = self.stream.read()
        crop_img = image[x:x+w,y:y+h ]
        cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)

        image = cv2.flip(image, 1)
        #ret,crop_img = cv2.imencode('.jpg',crop_img)
        cv2.imwrite('static/people_photo/fruit.jpg',crop_img)

        ret,jpeg = cv2.imencode('.jpg',image)

        cv2.imwrite('static/people_photo/image.jpg',image)
        data = [jpeg.tobytes()]
        return data
