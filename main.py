import random
import time
import tkinter as tk
from note_mapping import note_mapping



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