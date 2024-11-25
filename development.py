import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import filedialog
from tkinter import messagebox
import csv

class CreateTrackList:
    def __init__(self, window):
        window.geometry("750x600")
        window.title("Innovation Stage")
        window.configure(bg="lightblue")

        # Video Number
        number_lbl = tk.Label(window, text="Number:", bg="lightblue")
        number_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.number_txt = tk.Entry(window, width=5)
        self.number_txt.grid(row=0, column=1, padx=10, pady=10)

        # Name
        name_lbl = tk.Label(window, text="Name:", bg="lightblue")
        name_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.name_txt = tk.Entry(window, width=20)
        self.name_txt.grid(row=1, column=1, padx=10, pady=10)

        # Director
        director_lbl = tk.Label(window, text="Director:", bg="lightblue")
        director_lbl.grid(row=2, column=0, padx=10, pady=10)
        self.director_txt = tk.Entry(window, width=20)
        self.director_txt.grid(row=2, column=1, padx=10, pady=10)

        # Rating
        rating_lbl = tk.Label(window, text="Rating:", bg="lightblue")
        rating_lbl.grid(row=3, column=0, padx=10, pady=10)
        self.rating_txt = tk.Entry(window, width=5)
        self.rating_txt.grid(row=3, column=1, padx=10, pady=10)

        # Play count
        playcount_lbl = tk.Label(window, text="Play Count:", bg="lightblue")
        playcount_lbl.grid(row=4, column=0, padx=10, pady=10)
        self.playcount_txt = tk.Entry(window, width=5)
        self.playcount_txt.grid(row=4, column=1, padx=10, pady=10)

        # Scrolled Text for tracklist
        self.tracklist_text = tkst.ScrolledText(window, width=60, height=10)
        self.tracklist_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        # Status label for feedback
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="lightblue")
        self.status_lbl.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

        # Load data from CSV file after initializing all components
        self.load_tracklist_from_csv("listmusic.csv")

        # Buttons: Add Video, Play tracklist, and Reset tracklist on the same row
        add_track_btn = tk.Button(window, text="Add Track", command=self.add_video_to_tracklist)
        add_track_btn.grid(row=6, column=0, padx=10, pady=10)
        play_btn = tk.Button(window, text="Play Tracklist", command=self.play_tracklist, bg="white")
        play_btn.grid(row=6, column=1, padx=10, pady=10)
        reset_btn = tk.Button(window, text="Reset Tracklist", command=self.reset_tracklist, bg="white")
        reset_btn.grid(row=6, column=2, padx=10, pady=10)

        # Import button
        import_btn = tk.Button(window, text="Import", command=self.import_csv, bg="orange")
        import_btn.grid(row=7, column=0, padx=10, pady=10)

        # Delete button
        delete_btn = tk.Button(window, text="Delete ", command=self.delete_selected, bg="red", fg="white")
        delete_btn.grid(row=7, column=1, padx=10, pady=10)

         # Update button
        update_btn = tk.Button(window, text="Update", command=self.open_update_window, bg="green", fg="white")
        update_btn.grid(row=7, column=2, padx=10, pady=10)

        # Back button to return to main GUI
        back_btn = tk.Button(window, text="Back", command=window.destroy)
        back_btn.grid(row=9, column=0, columnspan=3, padx=10, pady=10)

    def add_video_to_tracklist(self):
        # Get the track number from the entry field
        track_number = self.number_txt.get()
        track_name = self.name_txt.get()

        # Validate the track number
        if not track_number.isdigit():
            self.status_lbl.configure(
                text="Error: Please enter track number.",
                fg="red",
                background="lightblue"
            )
            return

        # Insert the track name into the tracklist display
        self.tracklist_text.insert(tk.END, f"{track_name}\n")
        # Update status label with a confirmation message
        self.status_lbl.configure(
            text=f"Track {track_number} '{track_name}' added to tracklist.",
            fg="green",
            background="lightblue"
        )

    def play_tracklist(self):
        # Placeholder function for playing the tracklist
        self.status_lbl.configure(text="Playing Tracklist...")

    def reset_tracklist(self):
        # Clear the tracklist and reset the status label
        self.tracklist_text.delete(1.0, tk.END)
        self.status_lbl.configure(text="Tracklist has been reset.")

    def load_tracklist_from_csv(self, filename):
        try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)
                for row in reader:
                    self.tracklist_text.insert(tk.END, row[1] + "\n")
                self.status_lbl.configure(text="Tracklist loaded from file.")
        except FileNotFoundError:
            self.status_lbl.configure(text="File not found. Starting with an empty tracklist.")

    def import_csv(self):
        # Open file dialog to select a CSV file
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                with open(file_path, newline='', encoding='utf-8') as csvfile:
                    reader = csv.reader(csvfile)
                    next(reader)  # Skip header
                    self.tracklist_text.delete(1.0, tk.END)  # Clear current tracklist
                    for row in reader:
                        self.tracklist_text.insert(tk.END, row[1] + "\n")  # Add song name to tracklist
                    self.status_lbl.configure(text=f"tracklist imported from {file_path}.")
            except Exception as e:
                self.status_lbl.configure(text=f"Error importing file: {str(e)}")

    def delete_selected(self):
        try:
            # Get the selected text
            selected_text = self.tracklist_text.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
            # Find the line number of the selected text
            all_text = self.tracklist_text.get(1.0, tk.END).strip().split("\n")
            if selected_text in all_text:
                # Remove the selected song from the tracklist
                all_text.remove(selected_text)
                # Clear the tracklist and reinsert the updated list
                self.tracklist_text.delete(1.0, tk.END)
                for line in all_text:
                    self.tracklist_text.insert(tk.END, line + "\n")
                # Update the status label
                self.status_lbl.configure(text=f"Track '{selected_text}' deleted from tracklist")
        except tk.TclError:
            messagebox.showerror("Error", "No track selected. Please select a track to delete.")
    def open_update_window(self):  # [ADDED]
        update_window = tk.Toplevel() 
        UpdateTrackList(update_window, self) 

    def update_track(self, track_id, name, director, rating): 
        self.tracklist_text.insert(tk.END, f"{track_id}: {name} | Director: {director} | Rating: {rating}\n")
        self.status_lbl.configure(text=f"Track {track_id} updated successfully!", fg="green") 


class UpdateTrackList:
    def __init__(self, window, parent): 
        self.parent = parent 

        window.geometry("750x350") 
        window.title("Update Track") 
        window.configure(bg="skyblue") 

        # Number
        track_id_lbl = tk.Label(window, text="Number:", bg="skyblue") 
        track_id_lbl.grid(row=0, column=0, padx=10, pady=10) 
        self.track_id_txt = tk.Entry(window, width=5) 
        self.track_id_txt.grid(row=0, column=1, padx=10, pady=10) 

        # New music name
        name_lbl = tk.Label(window, text="Name:", bg="skyblue") 
        name_lbl.grid(row=1, column=0, padx=10, pady=10) 
        self.name_txt = tk.Entry(window, width=20) 
        self.name_txt.grid(row=1, column=1, padx=10, pady=10) 

        # Director
        director_lbl = tk.Label(window, text="Director:", bg="skyblue") 
        director_lbl.grid(row=2, column=0, padx=10, pady=10) 
        self.director_txt = tk.Entry(window, width=20) 
        self.director_txt.grid(row=2, column=1, padx=10, pady=10) 

        # Rating
        rating_lbl = tk.Label(window, text="Rating:", bg="skyblue") 
        rating_lbl.grid(row=3, column=0, padx=10, pady=10) 
        self.rating_txt = tk.Entry(window, width=3) 
        self.rating_txt.grid(row=3, column=1, padx=10, pady=10) 

        # Update button
        update_btn = tk.Button(window, text="Update", command=self.perform_update, bg="forestgreen") 
        update_btn.grid(row=4, column=1, padx=10, pady=10) 

        # Back button to return to main GUI
        back_btn = tk.Button(window, text="Back", command=window.destroy, bg="lightgray") 
        back_btn.grid(row=5, column=1, padx=10, pady=10) 

        # Status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="skyblue") 
        self.status_lbl.grid(row=6, column=0, columnspan=2, padx=10, pady=10) 

    def perform_update(self): 
        track_id = self.track_id_txt.get() 
        new_name = self.name_txt.get() 
        new_director = self.director_txt.get() 
        new_rating = self.rating_txt.get() 

        if not track_id or not new_name or not new_director or not new_rating: 
            self.status_lbl.configure(
                text="Error: All fields must be filled!", fg="red", background="skyblue"
            ) 
            return 

        try: 
            rating_value = float(new_rating) 
            if rating_value < 0 or rating_value > 10: 
                raise ValueError("Rating must be between 0 and 10.") 

            self.parent.update_track(
                track_id, new_name, new_director, new_rating
            ) 
            self.status_lbl.configure(
                text=f"Track {track_id} updated successfully!", fg="green", background="skyblue"
            ) 
        except ValueError as ve: 
            self.status_lbl.configure(text=f"Error: {ve}", fg="red", background="skyblue") 
    def add_track(self):
        number = self.number_txt.get()
        name = self.name_txt.get()
        if not number or not name:
            self.status_lbl.config(text="Error: Both fields must be filled!", fg="red")
            return
        self.tracklist_text.insert(tk.END, f"{number}: {name}\n")
        self.status_lbl.config(text=f"Track {number} added successfully!", fg="green")

   


# Run the application
window = tk.Tk()
app = CreateTrackList(window)
window.mainloop()
