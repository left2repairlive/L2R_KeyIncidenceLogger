from pynput.keyboard import Key, Listener
import csv
import datetime


# intro
print("==========================")
print("== Key Incidence Logger ==")
print("==    by Left2Repair    ==")
print("==========================")
print("")
print("Press ESC three times in a row to exit!")
print("")


# global vars
keylog = dict()
escCount = 0
timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


# Exit the program safely and save the data
def safe_exit():
    # print keylog results in terminal
    print("Results:")
    print(keylog)
    print("")

    print("Saving results as .csv ...")
    with open(timestamp + '.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key in keylog:
            writer.writerow([key, keylog[key]])
    print("DONE")
    print("")

    print("Saving results as keymap .png ...")
    print("NYI")
    print("")

    quit()


# What happens on a single keypress
def on_press(key):
    global escCount
    global keylog

    if str(key) == "Key.esc":
        escCount = escCount + 1
    else:
        escCount = 0

    if escCount >= 3:
        safe_exit()
        

    currentIncidince = keylog.get(key, 0)
    keylog[key] = currentIncidince + 1


# add key listener
with Listener(on_press=on_press) as listener:
    listener.join()

