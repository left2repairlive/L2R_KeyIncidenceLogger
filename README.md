# L2R_KeyIncidenceLogger
I wrote this Python program to log which keys I actually need during a gaming session. I'll use the results to design a custom keyboard layout which only incoorparates the keys I regularly use during gaming to minimize the layout.

## Usage
Simply start the program by running ```python ./KeyIncidinceLogger``` via a terminal. The program will run in the background and count how many times each key is pressed.

To stop the program, click ***Esc*** ten times in a row.

Each time the program is closed this way, it will create a timestamped output in from of a .csv table as well as a .png image of the results.

### .csv output
The *.csv* file holds the results as one key per row and the number of presses it registered for this key. This can be used for further processing if necessary

### .png output (*NYI*)
The *.png* file shows an ANSI 104 keyboard layout with a heatmap of how often any key is pressed. This gives a simple, visual overview of the results per key. Implementation for other keyboard layouts is not yet planned. Feel free to fork and implement anything yourself.

## Info about security
If concerned, please read through the code. The program only registers how often each key is pressed and writes the final results to the *.csv* and *.png* file, nowhere else! This does not include any order in which the keys are pressed.

**No info is saved or uploaded elsewhere, but only kept locally!**