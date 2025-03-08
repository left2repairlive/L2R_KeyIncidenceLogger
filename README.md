# L2R_KeyIncidenceLogger
I wrote this Python program to log which keys I actually need during a gaming session. I'll use the results to design a custom keyboard layout which only uses the keyboard shortcuts I regularly use during gaming to minimize the layout.

## Usage
Simply start the program with ```python ./KeyIncidinceLogger```. The program will work in the background and count how many time each key is pressed.
To stop the program, click **Esc** three times in a row. Each time the program is closed this way it will create a timestamped output in from of a .csv table as well as a .png image of the result.

## .csv output
The .csv file holds the results as one key per row and the number of presses it registered for this key. This can be used for further processing if necessary

## .png output (*NYI*)
The .png file shows an ANSI 101 keyboard layout with a heatmap of how often any key is pressed. This gives a simple overview of the keys. Implementation for other keyboard layouts is not yet planned. Feel free to fork and implement anything yourself.

## Info about security
If concerned, please read through the code. The program only looks how often which key is pressed and write the final results to the .csv and .png file. This does not include any order in which the keys are pressed.
No info is save or uploaded elsewhere, but only kept locally!