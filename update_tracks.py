import tkinter as tk

class UpdateTrackList:
    def __init__(self, window):
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
        update_btn = tk.Button(window, text="Update", command=self.update_track, bg="forestgreen")
        update_btn.grid(row=4, column=1, padx=10, pady=10)

        # Back button to return to main GUI
        back_btn = tk.Button(window, text="Back", command=window.destroy, bg="lightgray")
        back_btn.grid(row=5, column=1, padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="skyblue")
        self.status_lbl.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def update_track(self):
        track_id = self.track_id_txt.get()
        new_name = self.name_txt.get()
        new_director = self.director_txt.get()
        new_rating = self.rating_txt.get()

        # Input validation
        if not track_id or not new_name or not new_director or not new_rating:
            self.status_lbl.configure(
                text="Error: All fields must be filled!", 
                fg="red", 
                background="skyblue"
            )
        else:
            try:
                # Check if the rating is a valid number
                rating_value = float(new_rating)
                if rating_value < 0 or rating_value > 10:
                    raise ValueError("Rating must be between 0 and 10.")
                
                self.status_lbl.configure(
                    text=f"Track {track_id} updated successfully!", 
                    fg="green", 
                    background="skyblue"
                )
            except ValueError as ve:
                self.status_lbl.configure(
                    text=f"Error: {ve}", 
                    fg="red", 
                    background="skyblue"
                )

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = UpdateTrackList(root)
    root.mainloop()
