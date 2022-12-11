from PIL import Image
from news_manager import split_string
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFile
import time
import requests
import shutil
import PIL
from PIL import Image, ImageDraw, ImageFont

ImageFile.LOAD_TRUNCATED_IMAGES = True


def download_image(image_name, news_data):
    try:
        r = requests.get(news_data[2], stream=True)
        if r.status_code == 200:
            with open(f"images/{image_name}", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        else:
            print("Error")
    except requests.exceptions.MissingSchema:
        pass


def image_on_image(image, bg_image):
    try:
        img = Image.open(f"images/{image}", 'r')
    except FileNotFoundError:
        img = Image.open(f"base_files\\no_image.png", 'r')
    
    background= Image.open(f'base_files\{bg_image}', 'r')
    offset = (127, 146)
    background.paste(img, offset)
    background.save(f"images/{image}")

def image_size_changer(image_name):
    try:
        image = Image.open(f'images/{image_name}')
    except FileNotFoundError:
        pass
    else:
        sunset_resized = image.resize((1050, 790))
        sunset_resized.save(f'images/{image_name}')


def text_on_image(news_data, image_name):
    title=split_string(news_data[0], "title")
    content=split_string(news_data[3], "not")
    time.sleep(1)
    img = Image.open(r'images/'+image_name)
    
    I1 = ImageDraw.Draw(img)
    
    myFont = ImageFont.truetype('fonts/Raleway-Bold.ttf', 50)
    title_font= ImageFont.truetype('fonts\Raleway-ExtraBold.ttf', 60)
    z=1100
    for c in title:
        I1.text((135, z), c, font=title_font, fill =(0, 0, 0))
        z+=90
    z+=40
    for x in content:
        I1.text((135, z), x, font=myFont, fill =(0, 0, 0))
        z+=90
    img.save(f"images/{image_name}")


# # image_size_changer("no_image.png")

# print('PIL version:', PIL.__version__) 


# # create empty image
# img = Image.open("test\\business_bg.jpg")
# draw = ImageDraw.Draw(img)

# # draw white rectangle 200x100 with center in 200,150
# draw.rectangle((400-200, 300-100, 400+200, 300+100),fill="white")
# draw.line(((0, 150), (400, 150)), 'gray')
# draw.line(((200, 0), (200, 300)), 'gray')

# # find font size for text `"Hello World"` to fit in rectangle 200x100
# # selected_size = 1
# for size in range(1, 150):
#     arial = ImageFont.FreeTypeFont('fonts/Raleway-Bold.ttf', 50)
#     w, h = arial.getsize("Hello World")  # older versions
#     #left, top, right, bottom = arial.getbbox("Hello World")  # needs PIL 8.0.0
#     #w = right - left
#     #h = bottom - top
#     print(w, h)
    
#     if w > 200 or h > 100:
#         break
        
#     selected_size = size

#     print(arial.size)
    
# # draw text in center of rectangle 200x100        
# arial = ImageFont.FreeTypeFont('fonts/Raleway-Bold.ttf', 50)

# #draw.text((200-w//2, 150-h//2), "Hello World", fill='black', font=arial)  # older versions
# #img.save('center-older.png')

# draw.text((200, 150), "Hello World", fill='black', anchor='mm', font=arial)
# img.save('test\center-newer.png')

# img.show()