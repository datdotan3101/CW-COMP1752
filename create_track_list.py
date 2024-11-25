import tkinter as tk
import tkinter.scrolledtext as tkst
import csv


class CreateTrackList:
    def __init__(self, window):
        window.geometry("750x600")
        window.title("Create Track Playlist")
        window.configure(bg="lightblue")

        # Video Number
        number_lbl = tk.Label(window, text="Number:", bg="lightblue")
        number_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.number_txt = tk.Entry(window, width=10)
        self.number_txt.grid(row=0, column=1, padx=10, pady=10)

        # Name
        name_lbl = tk.Label(window, text="Name:", bg="lightblue")
        name_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.name_txt = tk.Entry(window, width=30)
        self.name_txt.grid(row=1, column=1, padx=10, pady=10)

        # Director
        director_lbl = tk.Label(window, text="Director:", bg="lightblue")
        director_lbl.grid(row=2, column=0, padx=10, pady=10)
        self.director_txt = tk.Entry(window, width=30)
        self.director_txt.grid(row=2, column=1, padx=10, pady=10)

        # Rating
        rating_lbl = tk.Label(window, text="Rating:", bg="lightblue")
        rating_lbl.grid(row=3, column=0, padx=10, pady=10)
        self.rating_txt = tk.Entry(window, width=10)
        self.rating_txt.grid(row=3, column=1, padx=10, pady=10)

        # Play Count
        playcount_lbl = tk.Label(window, text="Play Count:", bg="lightblue")
        playcount_lbl.grid(row=4, column=0, padx=10, pady=10)
        self.playcount_txt = tk.Entry(window, width=10)
        self.playcount_txt.grid(row=4, column=1, padx=10, pady=10)

        # Scrolled Text for Playlist
        self.playlist_text = tkst.ScrolledText(window, width=50, height=10)
        self.playlist_text.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

        # Status label for feedback
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="lightblue")
        self.status_lbl.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        # Load data from CSV file after initializing all components
        self.load_playlist_from_csv("listmusic.csv")

        # Buttons: Add Video, Play Playlist, and Reset Playlist
        add_track_btn = tk.Button(window, text="Add Track", command=self.add_video_to_playlist)
        add_track_btn.grid(row=7, column=0, padx=10, pady=10)

        play_btn = tk.Button(window, text="Play Playlist", command=self.play_playlist)
        play_btn.grid(row=7, column=1, padx=10, pady=10)

        reset_btn = tk.Button(window, text="Reset Playlist", command=self.reset_playlist)
        reset_btn.grid(row=7, column=2, padx=10, pady=10)

        # Back button
        back_btn = tk.Button(window, text="Back", command=window.destroy)
        back_btn.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

    def add_video_to_playlist(self):
        """Add video details to playlist."""
        number = self.number_txt.get()
        name = self.name_txt.get()
        director = self.director_txt.get()
        rating = self.rating_txt.get()
        play_count = self.playcount_txt.get()

        # Validate inputs
        if not (number and name and director and rating and play_count):
            self.status_lbl.config(text="Error: Please fill in all fields.", fg="red")
            return

        # Insert track into playlist display
        track_details = f"{name}\n"
        self.playlist_text.insert(tk.END, track_details)

        # Append to CSV file
        with open("listmusic.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([number, name, director, rating, play_count])

        self.status_lbl.config(text=f"Track '{name}' added to playlist.", fg="green")

        # Clear input fields
        self.number_txt.delete(0, tk.END)
        self.name_txt.delete(0, tk.END)
        self.director_txt.delete(0, tk.END)
        self.rating_txt.delete(0, tk.END)
        self.playcount_txt.delete(0, tk.END)

    def play_playlist(self):
        """Simulate playing the playlist."""
        self.status_lbl.config(text="Playing playlist...", fg="blue")

    def reset_playlist(self):
        """Reset playlist."""
        self.playlist_text.delete(1.0, tk.END)
        with open("listmusic.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Number", "Name", "Director", "Rating", "Play Count"])  # Add header
        self.status_lbl.config(text="Playlist has been reset.", fg="black")

    def load_playlist_from_csv(self, filename):
        """Load playlist from a CSV file."""
        try:
            with open(filename, newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header
                for row in reader:
                    self.playlist_text.insert(tk.END, f"{row[1]}\n")  # Display only track name
            self.status_lbl.config(text="Playlist loaded from file.", fg="green")
        except FileNotFoundError:
            self.status_lbl.config(text="File not found. Starting with an empty playlist.", fg="red")


# Run the application
if __name__ == "__main__":
    window = tk.Tk()
    app = CreateTrackList(window)
    window.mainloop()
