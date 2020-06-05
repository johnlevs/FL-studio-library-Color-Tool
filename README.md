# FL-studio-library-Color-Tool
A python script that colors the library browser folders in fl studio.  

To adjust the colors, edit the variables in the param.txt file shown below.
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