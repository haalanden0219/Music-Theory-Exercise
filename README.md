# Diatonic Scale Music Theory Tool

## Description

Project created to help a user be able to quickly identify the notes of diatonic scales to help them learn music theory. The current version has the user generate a major or minor scale by choice or random and be able to see the notes of that scale. We recently added a testing feature mode where the user is required to enter the notes by hand. We currently on support major and minor scales but are hoping to add more types. We currently have created a command line tool but want to design a gui executable in the future. The project is under development and more features will be added overtime.

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
- Running with no flags will print a random scale with a random root note.
``` python DSMTT.py ```
- Running with the note and/or --scale commands will let you choose a scale and root note.
``` python DSMTT.py --note C --scale Major```
- Running with the -t flag will put you into test mode.
``` python DSMTT.py -t ```

## Help
- Run code below for further help
 ```python DSMTT.py -h```

## Future Goals
- Create a gui executable for ease of access for non-programmers.
- Add a feature to test the 7 modes along side the scales.
- Implement an option to use flat notes instead of sharp.


## Authors
[Evan Haaland](https://www.linkedin.com/in/evannhaaland/) </br>
Connor Kreitzman
