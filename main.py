import random
import time
import tkinter as tk

# Define a dictionary to map notes to their corresponding string and fret positions
# Sharps (#) and Flats (b)
note_mapping = {
    'E': [('e', 0), ('B', 5), ('G', 9), ('E', 12)],
    'F': [('e', 1), ('A', 8), ('D', 3), ('E', 1)],
    'F#': [('e', 2), ('A', 9), ('D', 4), ('G', 11)],
    'Gb': [('e', 2), ('A', 9), ('D', 4), ('G', 11)],
    'G': [('e', 3), ('A', 10), ('D', 5), ('G', 0)],
    'Ab': [('e', 4), ('A', 11), ('D', 6), ('G', 1)],
    'G#': [('e', 4), ('A', 11), ('D', 6), ('G', 1)],
    'A': [('A', 0), ('D', 7), ('G', 2), ('B', 10)],
    'Bb': [('A', 1), ('D', 8), ('G', 3), ('B', 11)],
    'A#': [('A', 1), ('D', 8), ('G', 3), ('B', 11)],
    'B': [('A', 2), ('D', 5), ('G', 4), ('B', 0)],
    'C': [('A', 3), ('D', 6), ('G', 5), ('B', 1)],
    'Db': [('A', 4), ('D', 7), ('G', 6), ('B', 2)],
    'C#': [('A', 4), ('D', 7), ('G', 6), ('B', 2)],
    'D': [('D', 0), ('G', 7), ('B', 3), ('e', 10)],
    'Eb': [('D', 1), ('G', 8), ('B', 4), ('e', 11)],
    'D#': [('D', 1), ('G', 8), ('B', 4), ('e', 11)],
}

def display_large_note_and_answer():
    note = random.choice(list(note_mapping.keys()))
    positions = [f'{string}, {fret}' for string, fret in note_mapping[note]]
    
    # Update the label with the note
    label.config(text=f'Note: {note}')
    
    # Schedule the answer update after 4000 milliseconds (4 seconds)
    window.after(4000, update_answer_label, positions)

def update_answer_label(positions):
    # Update the label with the answer
    label.config(text='\n'.join(positions), font=("Helvetica", 36))
    
    # Schedule the next note display after 2000 milliseconds (2 seconds)
    window.after(2000, display_large_note_and_answer)

def main():
    global window, label
    
    # Create a Tkinter window
    window = tk.Tk()
    
    window.geometry("500x500")

    # Set the window title
    window.title("Neck Trainer")
    
    # Create a label with a large font to display the note and answer
    label = tk.Label(window, text="", font=("Helvetica", 72))
    label.pack(padx=20, pady=20)  # Add padding for better visibility

    # Start the cycle by scheduling the first note display
    display_large_note_and_answer()

    # Start the Tkinter main loop
    window.mainloop()

if __name__ == "__main__":
    main()