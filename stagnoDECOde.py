import stepic #for stagnoGraphy
from PIL import Image #for image import

file=input("PHOTO: ")

img= Image.open(file)

data=stepic.decode(img)

print("DATA: "+str(data))

print("*----------------------------*")     