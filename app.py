from ultralytics import YOLO
import cv2
import math 
import os
import google.generativeai as genai
import pyttsx3
import time

os.environ['GOOGLE_API_KEY'] = "<ENTER YOUR GEMINI API KEY>"
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

gemini_model = genai.GenerativeModel('gemini-pro')


# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 640)

# model
# model = YOLO("best.pt")
model = YOLO("pre-trained models/nadhim_asl.pt")



classNames = ["hello","I love you","please","yes","how","thanks","what","name","you"]

user_reply = []

def signTranslation():
    start_time = time.time()
    while True:
        success, img = cap.read()
        results = model(img, stream=True)

        # coordinates
        for r in results:
            boxes = r.boxes

            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # confidence
                confidence = math.ceil((box.conf[0]*100))/100
                print("Confidence --->",confidence)

                # class name
                cls = int(box.cls[0])
                print("Class name -->", classNames[cls])

                if confidence>=0.40:
                    user_reply.append(classNames[cls])

                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 2
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

        cv2.imshow('Webcam', img)
        end_time = time.time()
        if cv2.waitKey(1) == ord('q'):
            break

        # cv2.waitKey(500)
        # break
        if end_time-start_time>=4:
            break
        

def SpeakText(command):
     
    # Initialize the engine
    engine = pyttsx3.init()
    engine.setProperty('rate',145)
    # voices = engine.getProperty(voices)
    # engine.setProperty('voice',voices[-1].id)
    engine.say(command) 
    engine.runAndWait()
     

total_replies = ['  ']

while True:
    user_reply=[]
    unique_user_reply = []


    s = input("Enter ('s') to Sign Language: ").lower()
    if s!='s':
        print("Thank you for using this app!")
        SpeakText("Thank you for using this app!")
        break

    signTranslation()
    print()
    
    for i in user_reply:
        if i not in unique_user_reply:
            unique_user_reply.append(i)
    # unique_user_reply.append("?")
    #print(user_reply)
    #print(unique_user_reply)

    if len(total_replies)>3:
        total_replies = total_replies[2:]

    user_input = f'''generate a simple and coherent one line sentence using the words in the following list: {unique_user_reply}.
                    The words are generated after detecting the sign language reply of a deaf/dumb user, so frame the reply accordingly based on the limited vocabulary.
                    The context is having a casual conversation, so please keep it very very simple and understandable. You are acting as a mouth-piece for the user. 
                    Also, please be polite and mildly sophisticated as well. Thanks in advance!.
                    This has been the previous list of replies for more context: {total_replies}. While replying try to be more specific towards the context of the reply: {total_replies[-1]}.
                    Ignore context if previous reply is blank. '''
    
    user_input = f'''generate a simple and coherent one line sentence using the words in the following list: {unique_user_reply}.
    The words are generated after detecting the sign language reply of a deaf/dumb user, so frame the reply accordingly based on the limited vocabulary.
                    The context is having a casual conversation, so please keep it very very simple and understandable. You are acting as a mouth-piece for the user. '''
    response_data = gemini_model.generate_content(user_input)
    print("Detected Signs: ",unique_user_reply)
    print("Translated Coherent sentence: ", response_data.text)
    total_replies.append(response_data.text)
    SpeakText(response_data.text)

