import cv2
file = "image001.jpg"


image = cv2.imread(file)
if image.any() != None:
  if(len(image.shape)<2):
        print ('grayscale')
  elif len(image.shape)==3:
        print ('Colored')
else:
  print("cannot find image")  