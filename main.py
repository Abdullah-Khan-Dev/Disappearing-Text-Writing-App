import tkinter as tk
from threading import Timer

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("The Most Dangerous Writing App")

        self.text_area = tk.Text(root, font=("Helvetica", 14), wrap="word")
        self.text_area.pack(expand=True, fill="both")

        self.timer_label = tk.Label(root, text="Keep typing...", font=("Helvetica", 10))
        self.timer_label.pack()

        self.timer = None
        self.timeout_seconds = 5

        self.text_area.bind("<Key>", self.reset_timer)
        self.start_timer()

    def start_timer(self):
        if self.timer is not None:
            self.timer.cancel()
        self.timer = Timer(self.timeout_seconds, self.clear_text)
        self.timer.start()
        self.update_timer_label()

    def reset_timer(self, event):
        self.start_timer()

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)
        self.timer_label.config(text="Time's up! Text deleted!")
        self.start_timer()

    def update_timer_label(self):
        remaining_time = self.timer.interval if self.timer else self.timeout_seconds
        self.timer_label.config(text=f"Keep typing... {remaining_time:.1f}s remaining")
        self.root.after(100, self.update_timer_label)

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
