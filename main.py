import random
import tkinter as tk
from note_mapping import note_mapping

# Define a variable to track the pause state
paused = False
dark_mode = False  # Initially, set to light mode
note_count = 0  # Counter for the number of notes displayed


def toggle_pause():
    global paused
    paused = not paused
    if paused:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")
        # Resume the cycle
        display_large_note_and_answer()

def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        window.configure(bg="black")
        label.config(fg="white", bg="black")
        pause_button.config(bg="lightgray", fg="black")
        dark_mode_button.config(text="Light Mode", bg="lightgray", fg="black")
        cancel_button.config(text="Cancel", bg="lightgray", fg="black")
    else:
        window.configure(bg="white")
        label.config(fg="black", bg='white')
        pause_button.config(bg="lightgray", fg="black")
        dark_mode_button.config(text="Dark Mode", bg="lightgray", fg="black")
        cancel_button.config(text="Cancel", bg="lightgray", fg="black")

def display_large_note_and_answer():
    global note_count
    if not paused:
        note = random.choice(list(note_mapping.keys()))
        positions = [f'{string}, {fret}' for string, fret in note_mapping[note]]

        # Update the label with the note
        label.config(text=f'Note: {note}', font=("Helvetica", 72))

        # Schedule the answer update after 4000 milliseconds (4 seconds)
        window.after(4000, lambda: update_answer_label(positions, note))

        note_count += 1

        if note_count >= 3:
            stop_app()

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
    global window, label, pause_button, dark_mode_button, cancel_button

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

    # Create a dark mode toggle button
    dark_mode_button = tk.Button(window, text="Dark Mode", command=toggle_dark_mode)
    dark_mode_button.place(relx=1.0, rely=1.0, anchor="se", x=-150, y=-10)

    cancel_button = tk.Button(window, text="Cancel", command=stop_app)
    cancel_button.place(relx=1.0, rely=1.0, anchor="se", x=-60, y=-10)

    # Start the cycle by scheduling the first note display
    display_large_note_and_answer()

    # Start the Tkinter main loop
    window.mainloop()

if __name__ == "__main__":
    main()
