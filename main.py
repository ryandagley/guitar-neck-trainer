import random
import tkinter as tk
from note_mapping import note_mapping

# Define a variable to track the pause state
paused = False

def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")
        # Resume the cycle
        display_large_note_and_answer()

def display_large_note_and_answer():
    if not paused:
        note = random.choice(list(note_mapping.keys()))
        positions = [f'{string}, {fret}' for string, fret in note_mapping[note]]

        # Update the label with the note
        label.config(text=f'Note: {note}', font=("Helvetica", 72))

        # Schedule the answer update after 4000 milliseconds (4 seconds)
        window.after(4000, lambda: update_answer_label(positions, note))

def update_answer_label(positions, note):
    # Update the label with the answer
    text = f'{note} is located at: \n' + '\n'.join(positions)
    label.config(text=text, font=("Helvetica", 36))

    # Schedule the next note display after 2000 milliseconds (2 seconds)
    window.after(3000, display_large_note_and_answer)

def stop_app():
    global running
    running = False
    window.quit()

def main():
    global window, label, pause_button

    # Create a Tkinter window
    window = tk.Tk()
    window.geometry("500x500")
    window.title("Guitar Neck Trainer")
    
    # Create a label with a large font to display the note and answer
    label = tk.Label(window, text="", font=("Helvetica", 72))
    label.place(x=20, y=20)

    # Create a pause/unpause button
    pause_button = tk.Button(window, text="Pause", command=toggle_pause)
    pause_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    cancel_button = tk.Button(window, text="Cancel", command=stop_app)
    cancel_button.place(relx=1.0, rely=1.0, anchor="se", x=-60, y=-10)

    # Start the cycle by scheduling the first note display
    display_large_note_and_answer()

    # Start the Tkinter main loop
    window.mainloop()

if __name__ == "__main__":
    main()
