#Extension of project inspired by Connor Kreitzman

import random

def get_major_scale(root_note): 
    notes_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    root_index = notes_sharp.index(root_note)
    major_scale_intervals = [0, 2, 4, 5, 7, 9, 11]
    major_scale = [notes_sharp[(root_index + interval) % len(notes_sharp)] for interval in major_scale_intervals]
    return major_scale

def get_minor_scale(root_note): 
    notes_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    root_index = notes_sharp.index(root_note)
    minor_scale_intervals = [0, 2, 3, 5, 7, 8, 10]
    minor_scale = [notes_sharp[(root_index + interval) % len(notes_sharp)] for interval in minor_scale_intervals]
    return minor_scale


def main():

    notes_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    notes_flat = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

    guitar_note = random.choice(notes_sharp)
    guitar_string = random.randint(1,6) 

    types_of_scales = ['Major', 'Minor']
    type_of_scale = random.choice(types_of_scales)

    if type_of_scale == 'Major':
        print(guitar_note, type_of_scale,"Scale")
        created_scale = get_major_scale(guitar_note)
        print(created_scale)
    elif type_of_scale == 'Minor':
        created_scale = get_minor_scale(guitar_note)
        print(created_scale)
    elif type_of_scale == 'Harmonic Minor':
        created_scale = []
    elif type_of_scale == 'Melodic Minor':
        created_scale = []

if __name__ == "__main__":
    main()