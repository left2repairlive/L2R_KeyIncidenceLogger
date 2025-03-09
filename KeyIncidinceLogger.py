from pynput.keyboard import Key, Listener
import csv
import datetime
import json 
import math
import PIL
from PIL import Image, ImageDraw, ImageFont


# intro
print("==========================")
print("== Key Incidence Logger ==")
print("==    by Left2Repair    ==")
print("==========================")
print("")
print("Press ESC ten times in a row to exit!")
print("")



# global vars
keylog = dict()
escCount = 0
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
maxCount = 0



# function to exit program after saving results
def safe_exit():
    # print keylog results in terminal
    print("Results:")
    print(keylog)
    print("")

    write_csv()

    write_png()

    quit()



# function for exporting csv
def write_csv():
    global maxCount

    print("Saving results as .csv ...")

    with open(timestamp + '.csv', 'w+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key in keylog:
            count = keylog[key]
            writer.writerow([key, count])
            if(count > maxCount):
                maxCount = count

    print("DONE")
    print("")
    


# function for exporting png
def write_png():
    print("Saving results as keymap .png ...")
    
    with open('ANSI104.json') as jsonfile:
        jsonData = json.load(jsonfile)

        gridSize = jsonData['board']['gridSize']
        imageWidth = jsonData['board']['width'] * gridSize
        imageHeight = jsonData['board']['height'] * gridSize

        image = Image.new("RGB", (int(imageWidth), int(imageHeight)), "#444444")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 19)

        keysData = jsonData['keys']

        for key in keysData:
            keyID = key['keyID']
            keyLabel = key['keyLabel']
            
            keyX = key['x'] * gridSize
            keyY = key['y'] * gridSize

            keyWidth = 1 * gridSize
            if('width' in key):
                keyWidth = key['width'] * gridSize
            
            keyHeight = 1 * gridSize
            if('height' in key):
                keyHeight = key['height'] * gridSize
            
            keyCount = 0
            if(keyID in keylog):
                keyCount = keylog[keyID]
            keyHeat = math.log1p(keyCount) / math.log1p(maxCount)

            if(keyCount > 0):
                keyLabel = keyLabel + "/" + str(keyCount)

            keyDimensions = (keyX, keyY, keyX + keyWidth, keyY + keyHeight)
            keyFill = (16 * (keyHeat > 0) + int(239 * keyHeat), 0, 0)
            
            draw.rectangle(keyDimensions, fill=keyFill, outline="#000000")
            draw.text((keyX + 2, keyY + 2), keyLabel, "#FFFFFF", font = font)
            
        image.save(timestamp + ".png", "PNG")

    print("DONE")
    print("")


# function for how to process a keystroke
def on_press(key):
    global escCount
    global keylog

    currentIncidince = keylog.get(str(key), 0)
    keylog[str(key)] = currentIncidince + 1

    if str(key) == "Key.esc":
        escCount = escCount + 1
    else:
        escCount = 0

    if escCount >= 10:
        safe_exit()


# add key listener
with Listener(on_press=on_press) as listener:
    listener.join()
