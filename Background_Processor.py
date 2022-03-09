from PIL import Image, ImageFilter
import datetime
import os, sys, getopt

input_file=""
output_file=""

try:
      opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        sys.exit()
    elif opt in ("-i", "--ifile"):
        input_file = arg
    elif opt in ("-o", "--ofile"):
        output_file = arg

# filepath = "C:\\Development\\Python\\Images\\SeptemberBDays.jpg"
today = datetime.date.today()
image = Image.open(input_file)
rows = image.height
cols = image.width
white = (255,255,255)

firstPixel = 0
lastPixel = 0

for x in range(rows):
    rgb = image.getpixel((0, x))
    if firstPixel == 0 and rgb == white:
        firstPixel = x
    if rgb == white:
        lastPixel = x

print("Image height: " + str(image.height))
print("Image Width: " + str(image.width))
print("First white row: " + str(firstPixel))
print("Last white row: " + str(lastPixel))

for x in range(cols):
    for y in range(firstPixel):
        image.putpixel((x,y), white)
    for z in range(rows - lastPixel):
        image.putpixel((x,z+lastPixel), white)
        
image.show()
# Create name of the new file
newFilePath = "P:\\\\SALES WALLPAPER\\" + today.strftime("%B") + "BDays.jpg"
# Save the new background
# image.save(newFilePath)


# Moving the old background to the folder one
oldFileLoc = "P:\\\\SALES WALLPAPER\\" + (today.replace(day=1) - datetime.timedelta(days=1)).strftime("%B") + "BDays.jpg"
oldNewFileLoc = "P:\\\\SALES WALLPAPER\\wallpapers\\" + (today.replace(day=1) - datetime.timedelta(days=1)).strftime("%B") + "BDays.jpg"

os.replace(oldFileLoc, oldNewFileLoc)