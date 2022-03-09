# ImageFilter for using filter() function
from PIL import Image, ImageFilter

# Help: https://www.analyticsvidhya.com/blog/2014/12/image-processing-python-basics/
# Other Help: https://pillow.readthedocs.io/en/latest/handbook/tutorial.html#point-operations

# Opening the image
# (R prefixed to string in order to deal with the '\' in paths)

filepath = "C:\\Development\\Python\\Images\\rise.jpg"
image = Image.open(filepath)

# Blurring the image by sending the ImageFilter
# GaussianBlur predefined kernel argument

blurred_image = image.filter(ImageFilter.GaussianBlur)

# filter 10x
for x in range(10):
    blurred_image = blurred_image.filter(ImageFilter.GaussianBlur)

# Save image
blurred_image.save("C:\\Development\\Python\\Images\\blurred_image.jpg")

# Displaying the images
image.show()
blurred_image.show()


# Cropping & Blurring a small section of the image
# Cropping...

# sub_image = image.crop((0,0,150,150))

# blurring image
# blurred_sub_image = sub_image.filter(ImageFilter.GaussianBlur)

# Pasting blurred image onto original //don't do!!!
# image.paste(blurred_image, (0,0))

# Save & Display image
# blurred_sub_image.save("C:\\Development\\Python\\blurred_sub_image.jpg")
# sub_image.show()
# blurred_sub_image.show()



# image.save(filepath)

# reduce the value of every pixel by half
# image.point(lambda x: x * .5)
# image.show()

# map over each channel (r,g,b) on each pixel in the image
# def change_to_a_half(val):
#     return val // 2

# im = Image.open('./imagefile.jpg')
# im.point(change_to_a_half)