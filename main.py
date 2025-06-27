import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

last_action_time = 0
cooldown = 1

screen_w, screen_h = pyautogui.size()
cap = cv2.VideoCapture(0)
prev_x, prev_y = pyautogui.position()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)
    if result.multi_hand_landmarks:
        for hand_landmark in result.multi_hand_landmarks:

            x = hand_landmark.landmark[8].x * w
            y = hand_landmark.landmark[8].y * h

            x_thumb = hand_landmark.landmark[4].x * w
            y_thumb = hand_landmark.landmark[4].y * h

            distance = ((x_thumb - x) ** 2 + (y_thumb - y) ** 2) ** 0.5

            current_time = time.time()

            if distance < 40 and current_time - last_action_time > cooldown:
                print("Click by pinch in")
                pyautogui.doubleClick()
                last_action_time = current_time

            elif distance > 100 and current_time - last_action_time > cooldown:
                last_action_time = current_time

            screen_x = int(hand_landmark.landmark[8].x * screen_w)
            screen_y = int(hand_landmark.landmark[8].y * screen_h)

            smooth_x = prev_x + (screen_x - prev_x) * 0.3
            smooth_y = prev_y + (screen_y - prev_y) * 0.3

            smooth_x = max(0, min(smooth_x, screen_w - 1))
            smooth_y = max(0, min(smooth_y, screen_h - 1))

            pyautogui.moveTo(smooth_x, smooth_y)
            prev_x, prev_y = smooth_x, smooth_y

    time.sleep(0.01)

cap.release()
