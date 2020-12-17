import cv2
import os

try:
    os.mkdir("Output")
except FileExistsError:
    print("Directory already exists")

output_path = "Output/"
fruit = input("Enter fruit Name : ")
no_of_shots = 0
max_shots = int(input("Enter No of shots : "))

camera = cv2.VideoCapture(0)
x,y = 50,50
w,h = 200,200


while no_of_shots < max_shots:
    ret,image = camera.read()
    crop_img = image[x:x+w,y:y+h ]
    cv2.imwrite(output_path+fruit+"_"+str(no_of_shots)+'.jpg',crop_img)        
    cv2.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
    image = cv2.flip(image,1)
    cv2.imshow("Camera",image)


    cv2.waitKey(3000)
    no_of_shots+=1


camera.release()
cv2.destroyAllWindows()
