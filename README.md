# PaPiRus-PiHole

Display the **number of blocked requests, and filtered traffic**, from [Pi-Hole](https://pi-hole.net), on [PaPiRus](https://github.com/PiSupply/PaPiRus).

![Image PaPiRus-PiHole](https://raw.githubusercontent.com/53645714n/PaPiRus-Pihole/master/image.JPG)

- Setup **Pi-Hole**, follow the [installation instructions](https://learn.adafruit.com/pi-hole-ad-blocker-with-pi-zero-w/install-pi-hole).
- Setup **PaPiRus**, follow the [installation instructions](https://github.com/PiSupply/PaPiRus).
- Clone this repo on your [Raspberry Pi Zero W](https://www.raspberrypi.org/products/).

## Reload automatically every 30 minutes

Edit `crontab`. 

```
crontab -e
```

Add the following line:

```
*/30 * * * * python /home/PaPiRus-PiHole/main.py
```

Enjoy!
