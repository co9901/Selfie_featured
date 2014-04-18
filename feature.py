import sys
import Image, ImageDraw
import datetime

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

def getDate():
    today = datetime.date.today()
    dateString = today.strftime("%y%m%d")
    return dateString

def generate(background, user, country):
    counter = Image.open('counter.png')
    user = user.resize((218, 218), Image.ANTIALIAS)
    user = add_corners(user, 30)
    background.paste(user, (150, 100), user)
    background.paste(counter,(123, 78) ,counter)
    background.save('weekly_people_' + country + '_' + getDate() + '.png')
    return 


user_kor = Image.open(sys.argv[1])
user_twn = Image.open(sys.argv[2])
background_kor = Image.open('background/kor.png')
background_twn = Image.open('background/twn.png')

generate(background_kor, user_kor, 'kor')
generate(background_twn, user_twn, 'twn')



