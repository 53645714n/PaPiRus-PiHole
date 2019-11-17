import os
import json
import urllib2
import datetime
from papirus import PapirusComposite
from PIL import Image, ImageFont, ImageDraw


# Set current directory

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load graphic

img = './pihole-bw.bmp'
#draw = ImageDraw.Draw(img)

# get date
update = datetime.datetime.now()

# get api data

try:
  f = urllib2.urlopen('http://192.168.1.104/admin/api.php')
  json_string = f.read()
  parsed_json = json.loads(json_string)
  adsblocked = parsed_json['ads_blocked_today']
  ratioblocked = parsed_json['ads_percentage_today']
  f.close()
except:
  queries = '?'
  adsblocked = '?'
  ratio = '?'
  ratioblocked ='?'

# Calling PapirusComposite this way will mean nothing is written to the screen until WriteAll is called
textNImg = PapirusComposite(False)

# Write text to the screen at selected point, with an Id
# Nothing will show on the screen
textNImg.AddText(str(adsblocked), 5, 5, Id="blocked", size=45 )
textNImg.AddText(str("%.1f" % round(ratioblocked,2)) +"%", 5, 45, Id="percentage", size=45 )

# Add image
# Nothing will show on the screen
# textNImg.AddImg(path, posX,posY,(w,h),id)
textNImg.AddImg(img,120,5,(80,80), Id="pihole")

# Write text to the screen at selected point, with an Id
# Nothing will show on the screen
textNImg.AddText(str(update), 100, 85, Id="update", size=8 )

# Now display all elements on the screen
textNImg.WriteAll()
