import cv2
import numpy as np

def detect_traffic_light_color(image):
    # Convert image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define color ranges for red, yellow, and green in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    
    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])
    
    # Mask the image to only get the color regions
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    
    # Find contours in each mask
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Check if any contours are found
    if len(contours_red) > 0:
        return "Red"
    elif len(contours_yellow) > 0:
        return "Yellow"
    elif len(contours_green) > 0:
        return "Green"
    else:
        return "No Traffic Light Color Detected"


image =  cv2.imread('traffic light image.png')



color = detect_traffic_light_color(image)
print("Traffic Light Color:", color)


cv2.imshow('Traffic Light Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
