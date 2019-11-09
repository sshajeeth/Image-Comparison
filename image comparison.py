import cv2


def compare_image(img1, img2):
    image_1 = cv2.imread(img1)
    image_2 = cv2.imread(img2)

    if image_1.shape == image_2.shape:
        print("The images have same size and channels ")

    difference = cv2.subtract(image_1, image_2)
    b, g, r = cv2.split(difference)

    if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
        print("Both images are same")
    else:
        print("Both images are not same")


image_1 = "Enter Image 1 Path Here"
image_2 = "Enter Image 2 Path Here"
compare_image(image_1, image_2)
