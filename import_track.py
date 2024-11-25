import tkinter as tk
import font_manager as fonts

class ImportTrack:
    def __init__(self, window):
        window.geometry("400x200")
        window.title("Import Music")
        #Import video
        import_btn = tk.Button(window, text="Import Music", command=self.import_track)
        import_btn.grid(row=1, column=4, padx=10, pady=10)
        #Back to return main GUI
        back_btn = tk.Button(window, text="Back", command=window.destroy)
        back_btn.grid(row=20, column=2, padx=10, pady=10)
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    def import_track(self):
        file_path = self.file_path_txt.get()
        self.status_lbl.configure(text=f"Tracks imported from {file_path}!")
