# Author: Anthony Clemente
# Purpose: Use DNA combinations to hide a message (0123/CTAG encoding)
# Notes: Use scripture (chapter, verse) to start hide pixels in message
#        After that....every (1/(right-most digit of (chapter - verse)) of every B in RGB -> binary)'s LSB will contain
#        the next bit of (message -> binary)
# Steps: Convert message to binary (ASCII)
#        Encrypt using key (book)
#        Encyrpt Image as well
#        Life -> 01001100 01101001 01100110 01100101
#        'L' = 01001100 (76)
#        'i' = 01101001 (105)
#        'f' = 01100110 (102)
#        'e' = 01100101 (101)
# Ex: Life (without encryption)
# 0123/CTAG Encoding
#        C -> 00
#        T -> 01
#        A -> 10
#        G -> 11
#  Life -> 01 00 11 00     01 10 10 01    01 10 01 10    01 10 01 01 -> 
#  DNA Helix Strand Pairs...
#  (T <-> A)
#  (C <-> G)
#  (G <-> C)
#  etc.

# Hiding image within image...
# Every so pixels...change LSB to create real pixel
# Requirement: REALLY BIG image

from lib2to3.pytree import convert
from tkinter import X
from PIL import Image, ImageChops
import math
from cryptocode import encrypt, decrypt
import enchant

MAX_ENCRYPTED_CHARACTERS = 200
MAX_BITS = MAX_ENCRYPTED_CHARACTERS * 8

def convert_to_binary(var):
    if type(var) == str:
        return [format(ord(x), '08b') for x in var]
        # [bin(ord(x))[2:].zfill(8) for x in var]
    if type(var) == int:
        return format(var, '08b')
def max_image_bytes(image):
    # bytes = height * width * rgb / (# of bits in byte)
    return image.height * image.width * 3 // 8
def lsb_modification(pixel, lsb_value):
    # still need to convert entire pixel
    pixel = list(pixel)
    pixel[-1] = convert_binary_to_ascii(((convert_to_binary(pixel[-1]))[:7]) + str(lsb_value))
    return pixel
# def create_dna_pairs()
def is_english(string):
    d = enchant.Dict("en_US")
    return d.check(string)

def tuple_to_string(tup):
    s = ''
    for item in tup:
        s = s + item
    return s
def string_to_char_tuple(string):
    return [char for char in string]
def convert_binary_to_ascii(binary):
    binary_int = 0
    if(type(binary) == str):
        binary_int = int(binary, 2)
    return binary_int
def lsb_key_generator(book, chapter, verse):
    # defines pattern to which B of RGB values to modify lsb     
    lsb_key = len(book) + (chapter - verse)
    if(lsb_key == 0):
        lsb_key = 1.5
    elif(lsb_key < 0):
        lsb_key *= -1
    return lsb_key
def stego_implementation(image, chapter, verse, number_of_bits, lsb_key):
    # load image into tuple (pixels) for easier access
    pixels = image.load()
    x = chapter
    y = verse
    changed_pixels = list([])
    x_switch_counter = 0
    y_switch_counter = 0
    bits_tuple = string_to_char_tuple(tuple_to_string(convert_to_binary(message)))
    for bit in range(len(bits_tuple)):
        if [y,x] in changed_pixels:
            print("Collision! Counter: " + str(bit))
            break
        image.putpixel((y, x), tuple(lsb_modification(pixels[y,x], bits_tuple[bit])))
        changed_pixels.append([y,x])
        y = verse + math.ceil(math.ceil((verse+y_switch_counter)*math.pi)*lsb_key)
        y_switch_counter += 1
        if (y > image.width):
            x_switch_counter += 1
            x = chapter + math.ceil(math.ceil((chapter+x_switch_counter)*math.pi)*lsb_key)
            y = y % image.width
            y_switch_counter += 1
        if(x > image.height):
            while x > image.height:
                x = math.ceil((chapter + math.ceil(math.ceil((chapter+x_switch_counter)*math.pi)*lsb_key)) % image.height)
                x_switch_counter += 1
    return image
def stego_hiding(image, message, book, chapter, verse):    
    # max of 92 characters for encryption efficiency purposes
    if(len(encrypt(message, book)) <= MAX_ENCRYPTED_CHARACTERS):
        lsb_key= lsb_key_generator(book, chapter, verse)
        message = encrypt(message, book)
        number_of_bits = len(convert_to_binary(message)) * 8
        return stego_implementation(image, chapter, verse, number_of_bits, lsb_key)
    else:
        return False
def stego_analysis(image, book, chapter, verse):
    # defines pattern to which B of RGB values to modify lsb 
    lsb_key = lsb_key_generator(book, chapter, verse)
    if(lsb_key == 0):
        lsb_key = 1.5
    elif(lsb_key < 0):
        lsb_key *= -1


    x = chapter
    y = verse
    counter = 0
    x_switch_counter = 0
    y_switch_counter = 0
    message_bytes = list()
    byte_counter = 0

    # max of 200 encrypted characters for efficiency purposes, 8 bits in 1 byte
    for pix in range(MAX_ENCRYPTED_CHARACTERS * 8):
        pixel = (image.getpixel(tuple([y, x])))[-1]
        # get 'B' value of pixel and append LSB
        if(pix % 8 == 0):
            message_bytes.append((convert_to_binary(pixel))[-1])
            if(pix != 0):
                byte_counter += 1
        else:
            message_bytes[byte_counter] += ((convert_to_binary(pixel))[-1])
        
        counter += 1
        y = verse + math.ceil(math.ceil((verse+y_switch_counter)*math.pi)*lsb_key)
        y_switch_counter += 1
        if (y > image.width):
            x_switch_counter += 1
            x = chapter + math.ceil(math.ceil((chapter+x_switch_counter)*math.pi)*lsb_key)
            y = y % image.width
            y_switch_counter += 1
            if(x > image.height):
                while x > image.height:
                    x = math.ceil((chapter + math.ceil(math.ceil((chapter+x_switch_counter)*math.pi)*lsb_key)) % image.height)
                    x_switch_counter += 1   
    # print(message_bits)
    # message = tuple_to_string(tuple(message_bits))
    message = ""
    for byte in message_bytes:
        message += str(chr(convert_binary_to_ascii(byte)))
    print(message)
    message = decrypt(message, book)
    print("Bits Processed: " + str(counter))
    return message
def test_driver():
    book = "Leviticus"
    message = "You're not supposed to see it in the image"
    message +="\n"
    chapter, verse = 17, 14

    # read the image
    filepath = "C:\\Users\\anthony.clemente\\Downloads\\april2022.jpg"
    image = Image.open(filepath)
    old_pixels = image.load()
    new_image = stego_hiding(image, message,book,chapter, verse)
    image.show()
    new_image.show()
    if(new_image is False):
        print("Message is too large to encrypt")
    else:
        message = stego_analysis(new_image, book, chapter, verse)
    print(message)

test_driver()
# new_image.show()
""" 
diff = ImageChops.difference(image, new_image)

if diff.getbbox():
    print("images are different")
else:
    print("images are the same") """