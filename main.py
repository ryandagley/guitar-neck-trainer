import random
import time
import tkinter as tk

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

def display_large_note_and_answer(note, answer, label):
    label.config(text=note)
    label.update()
    time.sleep(4)
    label.config(text=answer, font=("Helvetica", 36))
    label.update()
    time.sleep(2)

def main():
    # Create a Tkinter window
    window = tk.Tk()
    
    window.geometry("500x500")

    # Set the window title
    window.title("Neck Trainer")
    
    # Create a label with a large font to display the note and answer
    label = tk.Label(window, text="", font=("Helvetica", 72))
    label.pack(padx=20, pady=20)  # Add padding for better visibility

    while True:
        # Generate a random note
        note = random.choice(list(note_mapping.keys()))
        
        # Get the possible positions for the note
        positions = [f'{string}, {fret}' for string, fret in note_mapping[note]]
        
        # Display the large note and answer
        display_large_note_and_answer(f'{note}', '\n'.join(positions), label)

        # Wait for a couple of seconds before the next note
        time.sleep(1)  # Adjust the delay as needed

if __name__ == "__main__":
    main()

