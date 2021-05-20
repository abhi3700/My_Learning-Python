'''
	About
	=====
	- open the image file
	- show the image
	- print the image format
	- print the image mode

'''
from PIL import Image

try:
	img = Image.open("./img/city_purple_car.png")	
	
	# show image
	img.show()

	# show the format
	print(img.format)

	# print the mode of image
	print(img.mode)

except FileNotFoundError:
	# raise e
	print(f'the image file is not found.')
