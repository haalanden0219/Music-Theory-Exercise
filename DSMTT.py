#Extension of project inspired by Connor Kreitzman
#Evan Haaland & Connoer Kreitzman

import random
import argparse

def get_major_scale(root_note): 
    notes_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    root_index = notes_sharp.index(root_note)
    major_scale_intervals = [0, 2, 4, 5, 7, 9, 11]
    major_scale = [notes_sharp[(root_index + interval) % len(notes_sharp)] for interval in major_scale_intervals] # wprk out algorithm
    return major_scale

def get_minor_scale(root_note): 
    notes_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    root_index = notes_sharp.index(root_note)
    minor_scale_intervals = [0, 2, 3, 5, 7, 8, 10]
    minor_scale = [notes_sharp[(root_index + interval) % len(notes_sharp)] for interval in minor_scale_intervals]
    return minor_scale
    

def random_note_scale(notes_sharp, types_of_scales):
    guitar_note = random.choice(notes_sharp)
    type_of_scale = random.choice(types_of_scales)
    print_scales(guitar_note, type_of_scale)


def print_scales(note, scale):
    if scale.upper() == 'MAJOR':
        print(note.upper(), "Major Scale")
        created_scale = get_major_scale(note.upper())
        for note in created_scale:
            print(note.upper(), end= ' ')
    elif scale.upper() == 'MINOR':
        print(note.upper() , "Minor Scale")
        created_scale = get_minor_scale(note.upper())
        for note in created_scale:
            print(note, end= ' ')
    elif scale.upper() == 'Harmonic Minor':
        created_scale = []
    elif scale.upper() == 'Melodic Minor':
        created_scale = []

def main():
    types_of_scales = ['MAJOR', 'MINOR'] 
    notes_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    parser = argparse.ArgumentParser(description="Diatonic Scale Music Theory Tool: A useful tool to learn diatonic scales")
    parser.add_argument("--note", help="Name of Note")
    parser.add_argument("--scale", help="Name of Scale Type")
    args = parser.parse_args()
    
    if args.note and args.scale:

        try: 
            if ((args.note.upper() in notes_sharp) and (args.scale.upper() in types_of_scales)): 
                print_scales(args.note , args.scale)
            else:
                print("Invalid Note and/or Scale")
        
        except Exception as e:
            print("An exception occurred:", str(e))
                
    else:
        random_note_scale(notes_sharp, types_of_scales)

if __name__ == "__main__":
    main()