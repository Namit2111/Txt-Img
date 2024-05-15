import PIL
from PIL import Image, ImageDraw, ImageEnhance
import random

class WebPage:
  def __init__(self, img_path, text="0", max_width=300):
    self.img = Image.open(img_path)
    self.org_img = Image.open(img_path)
    self.text = text
    self.current_index = 0
    width, height = self.img.size
    if width > max_width:
      new_width  = max_width
      new_height = round(new_width * height / width) 
      self.img = self.img.resize((new_width, new_height))
    self.pixels = self.img.load()

  def Random_Index(self):
    self.current_index = random.randint(0, len(self.text)-1)

  def Get_Letter(self):
    letter = self.text[self.current_index]
    self.current_index += 1
    if self.current_index == len(self.text):
      self.current_index = 0
    return letter
  
  def Create_Image(self, filename="processedimage"):
    width, height = self.img.size
    print(width,height)

    
    img = PIL.Image.new(mode="RGB", size=(width * 10, height * 10))
    I1 = ImageDraw.Draw(img)
 
    # Custom font style and font size
    #myFont = ImageFont.truetype('unispacebd.ttf', 12)

    row_amount = 0
    column_amount = 0

    col_max = 0

    for y in range(height):      # this row
        for x in range(width):   # and this row was exchanged
            if len(self.pixels[x, y]) == 3:
                r, g, b = self.pixels[x, y]
            else:
                r, g, b, _ = self.pixels[x, y]
            I1.text((column_amount, row_amount), self.Get_Letter(), fill=(r, g, b))

            column_amount += 7
        row_amount += 7
        if col_max < column_amount:
          col_max = column_amount
        column_amount = 0
        self.Random_Index()

    img = img.crop((0, 0, col_max, row_amount))
    #img.save("img.jpg")
    factor = 1.5 #brightens the image
    enhancer = ImageEnhance.Brightness(img)
    img_output = enhancer.enhance(factor)
    
    # img_output.save("tmp/"+filename+".jpg")
    return img_output

if __name__ == "__main__":
  webpage = WebPage("test.png","TEST")
  webpage.Create_Image()