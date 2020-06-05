# FL-studio-library-Color-Tool
A python script that colors the library browser folders in fl studio. The script does all the work of generating the .NFO files for each sub-directory, shown on [this forum post](https://forum.image-line.com/viewtopic.php?t=36492). The files generated are placed in the output folder, and the user must drag and drop these into the fl studio folder. This was written with Python 3.8.

To run the script, first you will need to edit the param.txt file show below.
~~~
GRADIENT
To switch between gradient and hue modes, change the first line to 'HUE' for hue and 'GRADIENT' 
for gradients. 
======================================================================
Directory location below. Example: DIRECTORY: C:\path\to\flstudio\sample\library
DIRECTORY: 

=========================VARIABLES FOR HUE===============================
Color parameters
Top and bottom are the bounds for the hue degree in the HSV color scale. 
The direction can be positive or negative. Numbers Must be between 0 and 360
TOP: 
BOTTOM: 

LIGHT & DARK refer to the percent black and white levels in the HSV scale. 
Enter a number between 0 and 100 for each. 
LIGHT: 
DARK: 

=========================VARIABLES FOR GRADIENT===============================
Enter the Hex code for the color without the # symbol 
C1: 
C2: 
~~~
Depending on the header, you will fill in the variables for the Gradient or hue section.
[Google's color picker](https://www.google.com/search?q=color+picker) can be helpful to find the color codes for either HSV or Hex formats. For the directory, make sure to follow the format specified with the slashes.
## Gradient Example
This was the outcome with a gradient between \#e82f1e and \#cd20e8. So in the param file:
### at the header:
~~~
GRADIENT
~~~
### In the gradient section:
~~~
=========================VARIABLES FOR GRADIENT===============================
Enter the Hex code for the color without the # symbol 
C1: e82f1e
C2: cd20e8
~~~
Which results in this in the library browser in Fl Studio 
\
![Image](screencaps/GRADIENT.PNG)
## Hue Example
Hue uses the HSV system to cycle through colors. Enter the top and bottom of the range of hues you would like, as well as the light and dark levels (the other two numbers in HSV). 
### at the header:
~~~
HUE
~~~
### In the gradient section:
Using the same two colors from the prior example, 
~~~
=========================VARIABLES FOR HUE===============================
Color parameters
Top and bottom are the bounds for the hue degree in the HSV color scale. 
The direction can be positive or negative. Numbers Must be between 0 and 360
TOP: 91
BOTTOM:5

LIGHT & DARK refer to the percent black and white levels in the HSV scale. 
Enter a number between 0 and 100 for each. 
LIGHT: 87
DARK: 91
~~~
Which results in this in the library browser in Fl Studio 
\
![Image](screencaps/HUE.PNG) \
Remember to refresh the browser after you run the script!
