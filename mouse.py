import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
draw_lines = mp.solutions.drawing_utils
screen_width,screen_height = pyautogui.size()
fit_y=0
while True:
    no_need, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame_height,frame_width,_ = frame.shape
    color_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(color_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            draw_lines.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id,landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                #print(x,y)
                if id == 8:
                    cv2.circle(img = frame, center=(x,y),radius = 10,color = (0,255,255))
                    fit_x = screen_width/frame_width*x
                    fit_y = screen_height/frame_height*y
                    pyautogui.moveTo(fit_x,fit_y)
                if id == 4:
                    cv2.circle(img = frame, center=(x,y),radius = 10,color = (0,255,255))
                    fitt_x = screen_width/frame_width*x
                    fitt_y = screen_height/frame_height*y
                    if abs(fit_y - fitt_y)<20:
                        pyautogui.click()
                        pyautogui.sleep(1)
    cv2.imshow("i m mouse",frame)
    cv2.waitKey(1)



