from PIL import Image
img = Image.open('pixelgame_color.png').convert('LA')
img.save('pixelgame_gray.png')