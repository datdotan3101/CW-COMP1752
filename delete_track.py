import tkinter as tk
import font_manager as fonts

class DeleteTrack:
    def __init__(self, window):
        window.geometry("600x500")
        window.title("Delete Track")
        window.configure(bg="lightblue")  # Thống nhất màu nền

        # Number music
        track_id_lbl = tk.Label(window, text="Number:", bg="lightblue", font=("Helvetica", 12))  # [Đồng bộ màu nền và font]
        track_id_lbl.grid(row=0, column=0, padx=10, pady=10)
        self.track_id_txt = tk.Entry(window, width=20)
        self.track_id_txt.grid(row=0, column=1, padx=10, pady=10)

        # Name music
        name_lbl = tk.Label(window, text="Name:", bg="lightblue", font=("Helvetica", 12))  # [Đồng bộ màu nền và font]
        name_lbl.grid(row=1, column=0, padx=10, pady=10)
        self.name_txt = tk.Entry(window, width=20)
        self.name_txt.grid(row=1, column=1, padx=10, pady=10)

        # Director
        director_lbl = tk.Label(window, text="Director:", bg="lightblue", font=("Helvetica", 12))  # [Đồng bộ màu nền và font]
        director_lbl.grid(row=2, column=0, padx=10, pady=10)
        self.director_txt = tk.Entry(window, width=20)
        self.director_txt.grid(row=2, column=1, padx=10, pady=10)

        # Delete button
        delete_btn = tk.Button(window, text="Delete", command=self.delete_track, bg="red", fg="black", font=("Helvetica", 10, "bold"))
        delete_btn.grid(row=3, column=1, padx=10, pady=10)

        # Back button to return to main GUI
        back_btn = tk.Button(window, text="Back", command=window.destroy, bg="lightgray", fg="black", font=("Helvetica", 10, "bold"))
        back_btn.grid(row=4, column=1, padx=10, pady=10)

        # Status label
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10), bg="lightblue", fg="green")  # [Đồng bộ màu nền và font]
        self.status_lbl.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def delete_track(self):
        track_id = self.track_id_txt.get()
        if track_id:  # [Kiểm tra nếu track_id được nhập]
            self.status_lbl.configure(text=f"Track {track_id} deleted!")  # [Thông báo thành công]
        else:
            self.status_lbl.configure(text="Error: Please enter a track number!", fg="red")  # [Thông báo lỗi]


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = DeleteTrack(root)
    root.mainloop()

