import sys
import Image, ImageDraw

def add_corners(im, rad):
    circle = Image.new('L', (rad * 8, rad * 8), 0)
    draw = ImageDraw.ImageDraw(circle)
    draw.ellipse((0, 0, rad * 8, rad * 8), fill=255)
    circle = circle.resize((rad * 2, rad * 2), Image.ANTIALIAS)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

background = Image.open(str(sys.argv[1]))
user = Image.open(sys.argv[2])
counter = Image.open('counter.png')

user = user.resize((145, 145), Image.ANTIALIAS)
user = add_corners(user, 20)

background.paste(user, (100, 66), user)
background.paste(counter,(82, 52) ,counter)
background.save('result.png')

