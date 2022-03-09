from PIL import Image, ImageEnhance

filepath = "C:\\Development\\Python\\Images\\background.jpg"
#read the image
image = Image.open(filepath)
image.show()

#image brightness enhancer
enhancer = ImageEnhance.Brightness(image)

factor = 1 # gives original image
image_output = enhancer.enhance(factor)
image_output.save('brightness_background_1.jpg')
image_output.show()

factor = 0.5 # darkens the image
image_output = enhancer.enhance(factor)
image_output.save('brightness_background_05.jpg')
# image_output.show()

factor = 1.5 # brightens the image
image_output = enhancer.enhance(factor)
image_output.save('brightness_background_1-5.jpg')
image_output.show()