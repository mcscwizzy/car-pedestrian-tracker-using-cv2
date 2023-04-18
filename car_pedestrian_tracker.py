import cv2

# set up file paths
video_file = "your_video.mp4"
pedestrian_tracker_file = "pedestrian_tracker.xml"
car_tracker_file = "car_tracker.xml"

# read the video

# import pedestrian and car tracker
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_tracker_file)
car_tracker = cv2.CascadeClassifier(car_tracker_file)

# eternally loop until q is pressed
while True:

    # vidoes are collection of images so we need to read this video as it comes in
    successful_video_read, frame = video.read()

    # if read is successful then convert video to greyscale
    if successful_video_read:
        grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break

    # get the coordinates for pedestrian and cars
    pedestrian_coordinates = pedestrian_tracker.detectMultiScale(grayscaled_image)
    car_coordinates = car_tracker.detectMultiScale(grayscaled_image)

    # draw the square on the greyscale image for pedestrian and car
    for (x, y, w, h) in car_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    for (x, y, w, h) in pedestrian_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # display the video feed in a window
    cv2.imshow(f"{video}", frame)
    key = cv2.waitKey(1)

    # exit program if the q key is pressed
    if key == 1 or key == 113:
        break

# release the wevcam resource
video.release()
