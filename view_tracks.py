import tkinter as tk
import tkinter.scrolledtext as tkst  

import track_library as lib  # Import custom library
import font_manager as fonts  # Import font manager 

# Function to update the text in a given text area
def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear existing text 
    text_area.insert(1.0, content)   # Insert the new content 

# TrackViewer class to display track information
class TrackViewer():
    def __init__(self, window):
        # Set up the main window 
        window.geometry("750x350")  # Set the size of the window
        window.title("View Tracks")  # Set the window title

        # "List All Tracks" button
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Label prompting user to input track number
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry widget for the user to input the track number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # "View Track" button 
        check_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        check_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # ScrolledText widget to list all available tracks (scrollable area)
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Text widget to display the details of a specific track
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Status label to provide feedback to the user 
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # List all tracks automatically when the window is created
        self.list_tracks_clicked()

    # Function to handle the "View Track" button click
    def view_tracks_clicked(self):
        key = self.input_txt.get()  # Get the track number 
        name = lib.get_name(key)    # Fetch the name of the track 
        if name is not None:
            artist = lib.get_artist(key)   # Fetch the artist for the track
            rating = lib.get_rating(key)   # Fetch the rating for the track
            play_count = lib.get_play_count(key)  # Fetch the play count for the track
            track_details = f"{name}\n{artist}\nrating: {rating}\nplays: {play_count}"  # Format track details
            set_text(self.track_txt, track_details)  # Display the track details
        else:
            set_text(self.track_txt, f"Track {key} not found")  # Display a "not found" message
        self.status_lbl.configure(text="View Track button was clicked!")  # Update the status label

    # Function to handle the "List All Tracks" button click
    def list_tracks_clicked(self):
        track_list = lib.list_all()  # Fetch the list of all tracks from the library
        set_text(self.list_txt, track_list)  # Display the list of tracks in the list text area
        self.status_lbl.configure(text="List Tracks button was clicked!")  # Update the status label

if __name__ == "__main__":
    window = tk.Tk() 
    fonts.configure()  
    TrackViewer(window) 
    window.mainloop()  