#Extension of project inspired by Connor Kreitzman
#Evan Haaland & Connor Kreitzman

import random
import argparse

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

def get_harmonic_minor_scale(root_note):
    notes_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    root_index = notes_sharp.index(root_note)
    harmonic_minor_scale_interval = [0, 2, 3, 5, 7, 8, 11]
    harmonic_minor_scale = [notes_sharp[(root_index + interval) % len(notes_sharp)] for interval in harmonic_minor_scale_interval] 
    return harmonic_minor_scale

def user_identify_scale(scale_under_test):
    user_built_scale = []
    success_counter = 0
    failure_counter = 0
    for note in scale_under_test:
            if success_counter == 0:
                user_answer = input("What is the root note in the scale? ")
            elif success_counter == 1:
                user_answer = input("What is the 2nd note in the scale? ")
            elif success_counter == 2:
                user_answer = input("What is the 3rd note in the scale? ")
            elif success_counter == 3:
                user_answer = input("What is the 4th note in the scale? ")
            elif success_counter == 4:
                user_answer = input("What is the 5th note in the scale? ")
            elif success_counter == 5:
                user_answer = input("What is the 6th note in the scale? ")
            elif success_counter == 6:
                user_answer = input("What is the 7th note in the scale? ")
            if (user_answer.upper() == note ):
                user_built_scale.append(note)
                for sub_note in user_built_scale:
                    print(sub_note.upper(), end= ' ')
                print()
                print(user_answer.upper() , "is correct!")
                success_counter = success_counter + 1
                failure_counter = 0
            else: 
                print(user_answer, "is NOT correct!")
                failure_counter = failure_counter + 1
                print("The correct notes are:")
                for note in scale_under_test:
                    print(note.upper(), end= ' ')
                print("\nExiting Program")
                exit()

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
    elif scale.upper() == 'HARMONIC MINOR':
        print(note.upper() , "Harmonic Minor Scale")
        created_scale = get_harmonic_minor_scale(note.upper())
        for note in created_scale:
            print(note, end= ' ')
    elif scale.upper() == 'Melodic Minor':
        created_scale = []

def test_scale(note, scale):
    print("Welcome to Test Mode!")
    if scale.upper() == 'MAJOR':
        print(note.upper(), "Major Scale")
        created_scale = get_major_scale(note.upper())
        user_identify_scale(created_scale)
    elif scale.upper() == 'MINOR': 
        print(note.upper() , "Minor Scale")
        created_scale = get_minor_scale(note.upper())
        user_identify_scale(created_scale)
    elif scale.upper() == 'HARMONIC MINOR':
        print(note.upper(), "Harmonic Minor Scale")
        created_scale = get_harmonic_minor_scale(note.upper())
        user_identify_scale(created_scale)
    elif scale.upper() == 'Melodic Minor':
        created_scale = []

def main():
    types_of_scales = ['MAJOR', 'MINOR' , 'HARMONIC MINOR'] 
    notes_sharp = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    try:
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
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt detected. Exiting program.")
if __name__ == "__main__":
    main()