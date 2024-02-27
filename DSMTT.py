#Extension of project inspired by Connor Kreitzman
#Evan Haaland & Connor Kreitzman


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

def test_scale(note, scale):
    print("Welcome to Test Mode!")
    if scale.upper() == 'MAJOR':
        print(note.upper(), "Major Scale")
        created_scale = get_major_scale(note.upper())
        for note in created_scale:
            user_answer = input("What is the next note in the scale? ")
            if (user_answer.upper() == note ):
                print(user_answer , "is correct!")
            else:
                print(user_answer, "is NOT correct!")
                for note in created_scale:
                    print(note.upper(), end= ' ')
                print("Exiting Program")
                exit()
    elif scale.upper() == 'MINOR': 
        print(note.upper() , "Minor Scale")
        created_scale = get_minor_scale(note.upper())
        for note in created_scale:
            user_answer = input("What is the next note in the scale? ")
            if (user_answer.upper() == note ):
                print(user_answer.upper() , "is correct!")
            else:
                print(user_answer.upper(), "is NOT correct!")
                for note in created_scale:
                    print(note.upper(), end= ' ')
                print("Exiting Program")
                exit()
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
    parser.add_argument("-t" ,"--test", action="store_true", help="Enables test mode")

    args = parser.parse_args()

    if args.note and args.scale:
        try: 
            if ((args.note.upper() in notes_sharp) and (args.scale.upper() in types_of_scales)): 
                if args.test:
                    test_scale(args.note , args.scale)
                else:
                    print_scales(args.note , args.scale)
            else:
                print("Invalid Note and/or Scale")
        except Exception as e:
            print("An exception occurred:", str(e))
    
    elif args.note:        
        try: 
            if (args.note.upper() in notes_sharp ): 
                random_scale = random.choice(types_of_scales)
                if args.test:
                    test_scale(args.note , random_scale)
                else:
                    print_scales(args.note , random_scale)
            else:
                print(args.note, "is not a valid note")
        
        except Exception as e:
            print("An exception occurred:", str(e))
    
    elif args.scale: 
        try: 
            if (args.scale.upper() in types_of_scales ): 
                random_note = random.choice(notes_sharp)
                if args.test:
                    test_scale(random_note , args.scale)
                else:
                    print_scales(random_note , args.scale)
            else:
                print(args.scale, "is not a valid scale")
        
        except Exception as e:
            print("An exception occurred:", str(e))
    
    else:
        random_note = random.choice(notes_sharp)
        random_scale = random.choice(types_of_scales)
        if args.test:
            test_scale(random_note, random_scale)
        else:
            print_scales(random_note, random_scale)

if __name__ == "__main__":
    main()