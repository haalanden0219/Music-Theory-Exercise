# Diatonic Scale Music Theory Tool

## Description

Project created to help a user be able to quickly identify the notes of diatonic scales to help them learn music theory. The current version has the user generate a major, minor or harmonic minor scale by choice or random and be able to see the notes of that scale. We recently added a testing feature mode where the user is required to enter the notes by hand. We currently only support major, minor, and harmonic diatonic using sharp notes. We currently have created a command line tool but want to design a gui executable in the future. The project is under development and more features will be added overtime.

### Testing
One of the main goals we wanted with the tool is the ability to test one's knowlege of being able to figure out the notes of the scale by memory. This is to help someone understand the intervals of how the scales are made. For our test we currently have the user select test mode and enter the scale and/or note they want to attempt. If no note or scale is selected they will get a random test. Currently, the user only gets one attempt at guessing each note. 
## Getting Started

### Dependencies
- Python Installed
- Argparse python library
- Random python library

### Installing
- Check to make sure python is installed
- Download DSMTT.py
- Download imported libraries if not already installed

### Executing Program
- Running with no flags will print a random scale with a random root note. </br>
``` python DSMTT.py ``` </br>
- Running with the note and/or --scale commands will let you choose a scale and root note. </br>
``` python DSMTT.py --note C --scale Major``` </br>
> **Note:** The argument for harmonic minor scale must be entered in quotes like "Harmonic Minor" to be registered as the whole argument. </br>
- Running with the -t flag will put you into test mode. </br>
``` python DSMTT.py -t ``` </br>
 

## Help
- Run code below for further help </br>
 ```python DSMTT.py -h``` </br>

## Future Goals
- Create a gui executable for ease of access for non-programmers.
- Add a feature to test the 7 modes along side the scales.
- Implement an option to use flat notes instead of sharp.
- Implement an option where the user can modify testing parameters


## Authors
[Evan Haaland](https://www.linkedin.com/in/evannhaaland/) </br>
Connor Kreitzman
