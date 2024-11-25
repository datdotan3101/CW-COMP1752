import tkinter as tk
from create_track_list import CreateTrackList
from update_tracks import UpdateTrackList
from view_tracks import TrackViewer 

# Main GUI
window = tk.Tk()
window.geometry("720x250")
window.title("JukeBox")
window.configure(bg="gray")

# Define `status_lbl` at the top
status_lbl = tk.Label(window, bg='gray', text="", font=("Helvetica", 10)) 
status_lbl.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

# Clear status label
def clear_status():  
    status_lbl.configure(text="") 

# Open Create Track List window when the button is clicked
def create_tracks_clicked():
    status_lbl.configure(text="Track is created!")
    window.after(3000, clear_status)
    CreateTrackList(tk.Toplevel(window)) 

# Open Update Track window when the button is clicked
def update_tracks_clicked():
    status_lbl.configure(text="Track is updated!")
    window.after(3000, clear_status)
    UpdateTrackList(tk.Toplevel(window))  

# Open View Track window when the button is clicked
def view_tracks_clicked():
    status_lbl.configure(text="View Track button was clicked!")
    TrackViewer(tk.Toplevel(window)) 

# Header label
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Buttons
create_track_list_btn = tk.Button(window, text="Create Track List", command=create_tracks_clicked)
create_track_list_btn.grid(row=1, column=0, padx=10, pady=10)

update_tracks_btn = tk.Button(window, text="Update Track", command=update_tracks_clicked)
update_tracks_btn.grid(row=1, column=1, padx=10, pady=10)

# "View Tracks" Button 
view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=2, padx=10, pady=10) 

window.mainloop() 
