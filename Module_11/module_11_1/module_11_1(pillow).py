from PIL import Image
from PIL import ImageDraw, ImageFont


# Разворот изображения на 180 градусов и отдельное сохранение изменённого изображения
def rotate_image(name):
    with Image.open(f'{name}.jpg') as im:
        im.rotate(180).save('image_rotate.jpg')


# Изменение изображения сохраняя пропорции изображения, задавая только длину
def resize_image(name):
    with Image.open(f'{name}.jpg') as im:
        width, height = im.size
        new_width = 1200
        new_height = int(new_width * height / width)
        im.resize((new_width, new_height)).save('image_resize.jpg')


# Сохранение изображения в другом формате (в данном случае png)
def convert_image(name):
    with Image.open(f'{name}.jpg') as im:
        im.save('convert_image.png', 'png')


# Добавление текста(надписи) на фотографию
def text_image(name):
    with Image.open(f'{name}.jpg') as im:
        i_draw = ImageDraw.Draw(im)
        text = 'Tunnel of code'
        font = ImageFont.truetype('arial.ttf', size=100)
        i_draw.text((100, 100), text, font=font)
        im.save(f'{name}_text.jpg')


rotate_image('image1')
resize_image('image1')
convert_image('image1')
text_image('image1')
