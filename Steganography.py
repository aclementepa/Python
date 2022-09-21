import cv2
import math
from PIL import Image


def stego(filepath, message):
    image = cv2.imread(filepath)
    data = message
    # break it down now
    # convert the message to an array of ascii values


    # Calculate requirements for image size
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = image.shape

    pixels = len(data) * 3
    rows = math.ceil(pixels/width)

    count = 0
    chars = 0

    # loop through each pixel and byte

    for i in range(rows + 1):
        while (count < width and chars < len(data)):
            char = data[chars]
            chars += 1

            for index_k, k in enumerate(char):
                if((k=='1' and image[i][count][index_k % 3] % 2 == 0) or (k == '0' and image[i][count][index_k % 3] % 2 == 1)):
                    image[i][count][index_k % 3] -=1
                if(index_k % 3 == 2):
                    count += 1
                if(index_k == 7):
                    if(chars * 3 < pixels and image[i][count][2] % 2 == 1):
                        image[i][count][2] -= 1
                    if(chars*3 >= pixels and image[i][count][2] % 2 == 0):
                        image[i][count][2] -= 1
                    count += 1
        count = 0

    new_file_path = "C:\\Users\\anthony.clemente\\Downloads\\encrypted_image.jpg"
    cv2.imwrite(new_file_path, image)

    return new_file_path

def encrypt():
    return False

def decrypt():
    return True
    
filepath = "C:\\Users\\anthony.clemente\\Downloads\\download.bmp"
message = "Hello there ladies and gentlemen!"

new_file = stego(filepath, message)
Image.open(filepath).show()
Image.open(new_file).show()