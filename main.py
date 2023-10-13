import random
import time
import os

# Define a dictionary to map notes to their corresponding string and fret positions
# Sharps (#) and Flats (b)
note_mapping = {
    'E': [('e', 0), ('A', 5), ('D', 7), ('G', 12)],
    'F': [('e', 1), ('A', 6), ('D', 8), ('G', 13)],
    'F#': [('e', 2), ('A', 7), ('D', 9), ('G', 14)],
    'Gb': [('e', 2), ('A', 7), ('D', 9), ('G', 14)],
    'G': [('e', 3), ('A', 8), ('D', 10), ('G', 15)],
    'Ab': [('e', 3), ('A', 8), ('D', 10), ('G', 15)],
    'G#': [('e', 4), ('A', 9), ('D', 11), ('G', 16)],
    'A': [('A', 0), ('D', 5), ('G', 7), ('B', 12)],
    'Bb': [('A', 1), ('D', 6), ('G', 8), ('B', 13)],
    'A#': [('A', 1), ('D', 6), ('G', 8), ('B', 13)],
    'B': [('A', 2), ('D', 7), ('G', 9), ('B', 14)],
    'C': [('A', 3), ('D', 8), ('G', 10), ('B', 15)],
    'Db': [('A', 3), ('D', 8), ('G', 10), ('B', 15)],
    'C#': [('A', 4), ('D', 9), ('G', 11), ('B', 16)],
    'D': [('D', 0), ('G', 5), ('B', 7), ('e', 12)],
    'Eb': [('D', 1), ('G', 6), ('B', 8), ('e', 13)],
    'D#': [('D', 1), ('G', 6), ('B', 8), ('e', 13)],
}


def main():
    while True:
        # Generate a random note
        note = random.choice(list(note_mapping.keys()))
        
        # Print the note
        print(f'Note: {note}')

        # Wait 3 seconds before showing location of note.
        time.sleep(3)
        
        # Get the possible positions for the note
        positions = [f'String: {string}, Fret: {fret}' for string, fret in note_mapping[note]]
        
        # Print all possible positions
        print('\n'.join(positions))
        
        # Wait for a couple of seconds before the next note
        time.sleep(2)

        # Clear the output for the next one.
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
