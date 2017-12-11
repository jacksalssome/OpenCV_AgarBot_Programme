import cv2
import numpy as np
import time
import win32api, win32con
<<<<<<< HEAD
<<<<<<< HEAD
=======
#import pytesseract
>>>>>>> bbb2c551a3ac85881c596c772d12a5e4e918ff78
=======
#import pytesseract
>>>>>>> bbb2c551a3ac85881c596c772d12a5e4e918ff78
from grabscreen import grab_screen

screen_sizex = 1650
screen_sizey = 1080


#import screencapture
def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_RGB2BGR)
    #processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300) ## to see raw
    processed_img= cv2.GaussianBlur(processed_img, (3,3),0)


    # Set up the SimpleBlobdetector with default parameters.
    params = cv2.SimpleBlobDetector_Params()
    # Change thresholds
    #params.minThreshold = 0;
    #params.maxThreshold = 256;
    # Filter by Area.
    params.filterByArea = True
    params.minArea = 50
    # Filter by Circularity
    params.filterByCircularity = True
    params.minCircularity = 0.1
    # Filter by Convexity
    params.filterByConvexity = True
    params.minConvexity = 0.2
    # Filter by Inertia
    #params.filterByInertia = Truelinalg.norm
    params.minInertiaRatio = 0.2

    detector = cv2.SimpleBlobDetector_create(params)
    # Detect blobs.
    keypoints = detector.detect(processed_img)


    # Thanks to https://stackoverflow.com/users/5087436/alexander-reynolds
    # Find nearest food.
    pt = np.array([(screen_sizex / 2), (screen_sizey / 2)])
    nearest_kp = min(keypoints, key=lambda kp: np.linalg.norm(kp.pt - pt))

    #win32api.SetCursorPos((int(nearest_kp.pt[0]), (int(nearest_kp.pt[1]))))


    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    #processed_img = cv2.drawKeypoints(processed_img, keypoints, np.array([]), (255, 0, 0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    return processed_img

#countdown
for i in list(range(3))[::-1]:
    print(i+1)
    time.sleep(1)

#output commmands
def click(x,y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

last_time = time.time()
while(True):
<<<<<<< HEAD
<<<<<<< HEAD
    screen = grab_screen(region=(0,0, screen_sizex, screen_sizey))

    new_screen = process_img(screen)

=======
    screen = grab_screen(region=(0, 0, 1680, 1050))
=======
    screen = grab_screen(region=(0, 0, 1680, 1050))

    new_screen = process_img(screen)

    cv2.resize(new_screen, (100,50))
>>>>>>> bbb2c551a3ac85881c596c772d12a5e4e918ff78

    new_screen = process_img(screen)

    cv2.resize(new_screen, (100,50))

>>>>>>> bbb2c551a3ac85881c596c772d12a5e4e918ff78
    #FPS
    print('Frame Time: {}'.format((time.time() - last_time))) #Broken
    last_time = time.time()

    #cv2.imshow('window', new_screen)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    cv2.destroyAllWindows()
    #    break








