from PIL import Image
img=Image.open("ca.png").convert("JPEG").save("ca.jpg")
img