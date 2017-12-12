import cv2
import numpy as np
import time
import win32api, win32con
from grabscreen import grab_screen

skip_input = False
doonce = 0

print("Welcome to The AgarBot Programme!")

if skip_input == False:

    autoscreenx = win32api.GetSystemMetrics(0)
    autoscreeny = win32api.GetSystemMetrics(1)

    auto_screen_y_n = (input("Is your screen resulution: " + str(autoscreenx) + "x" + str(autoscreeny) + "? (y/n): "))

    if auto_screen_y_n == "y" or "Y" or "YES" or "yes" or "Yes": #Classic VisualBasic
        screen_sizex = autoscreenx
        screen_sizey = autoscreeny
    else:
        screen_sizex = int(input("Enter your horizontal screen resolution: "))
        screen_sizey = int(input("Enter your vertical screen resolution: "))
else:
    screen_sizex = 1680
    screen_sizey = 1050

#import screencapture
def process_img(original_image):

    processed_img = cv2.GaussianBlur(original_image, (3,3),0)
    processed_img = cv2.cvtColor(processed_img, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2=300)

    # Set up the SimpleBlobdetector with default parameters.
    params = cv2.SimpleBlobDetector_Params()
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 50
    params.maxArea = 700

    detector = cv2.SimpleBlobDetector_create(params)
    # Detect blobs.
    keypoints = detector.detect(processed_img)


    # Thanks to https://stackoverflow.com/users/5087436/alexander-reynolds
    # Find nearest food.
    pt = np.array([(screen_sizex / 2), (screen_sizey / 2)])
    nearest_kp = min(keypoints, key=lambda kp: np.linalg.norm(kp.pt - pt))

    #win32api.SetCursorPos((int(nearest_kp.pt[0]), (int(nearest_kp.pt[1]))))

    im2, contours, hierarchy = cv2.findContours(processed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    processed_img = cv2.drawContours(original_image, contours, -1, (0, 255, 0), 2)
    processed_img = cv2.drawKeypoints(original_image, keypoints, np.array([]), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    processed_img = cv2.circle(original_image, (int(nearest_kp.pt[0]), (int(nearest_kp.pt[1]))), 10, (0,0,255), -1)
    processed_img = cv2.circle(original_image, (int(screen_sizex / 2), int(screen_sizey / 2)), 10, (0, 255, 0), -1)

    return processed_img

#countdown#
for i in list(range(3))[::-1]:
    print(i+1)
    time.sleep(1)

#output commmands
def click(x,y):
    win32api.SetCursorPos((x,y))

last_time = time.time()
while(True):
    screen = grab_screen(region=(0,0, screen_sizex, screen_sizey))

    new_screen = cv2.resize(process_img(screen), (int(screen_sizex / 1.1), int(screen_sizey / 1.1)))

    #FPS
    print('Frame Time: {}'.format((time.time() - last_time))) #Broken
    last_time = time.time()

    cv2.imshow('window', new_screen)

    if doonce == 0:
        cv2.moveWindow('window', -900, 0)
        doonce = 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
