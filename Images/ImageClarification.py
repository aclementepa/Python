from PIL import Image, ImageEnhance

filepath = "C:\\Development\\Python\\Images\\background.jpg"
image = Image.open(filepath)
enhancer = ImageEnhance.Sharpness(image)

image.show()

# While a factor of 1 gives original image. factor>1 sharpens the image while factor<1 blurs the image.


# enhanced by a factor of 1
factor = 1
enhanced_image = enhancer.enhance(factor)
enhanced_image.save('enhanced_background_1.jpg')
enhanced_image.show()

# unenhanced by a factor of .05
factor = .05
enhanced_image = enhancer.enhance(factor)
enhanced_image.save('enhanced_background_05.jpg')
# enhanced_image.show()

# enhanced by a factor of 2
factor = 2
enhanced_image = enhancer.enhance(factor)
enhanced_image.save('enhanced_background_2.jpg')
enhanced_image.show()