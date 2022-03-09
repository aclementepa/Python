from PIL import Image, ImageEnhance

image = Image.open("C:\\Development\\Python\\Images\\background.jpg")

enhancer = ImageEnhance.Contrast(image)

# original image
factor = 1
enhanced_image = enhancer.enhance(factor)
enhanced_image.save('contrast_background_1.jpg')
enhanced_image.show()

# decrease contrast by a factor of .5
factor = .5
enhanced_image = enhancer.enhance(factor)
enhanced_image.save('contrast_background_5.jpg')
# enhanced_image.show()

# increase contrast by a factor of 1.1
factor = 1.1
enhanced_image = enhancer.enhance(factor)
enhanced_image.save('contrast_background_2.jpg')
enhanced_image.show()