# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python
from PIL import Image
from pathlib import Path


ROOT_FOLDER = Path(__file__).parent
IMAGE = ROOT_FOLDER / 'image.jpg'
NEW_IMAGE = ROOT_FOLDER / 'new_image.jpg'

pil_image = Image.open(IMAGE)

width, height = pil_image.size
exif_image = pil_image.getexif()

# width  new_width
# height new_height
new_width = round(width * 0.50)
new_heiht = round(height * 0.50)

new_image = pil_image.resize(size=(new_width, new_heiht))
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=100,
    exif=exif_image
)