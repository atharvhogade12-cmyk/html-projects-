import tkinter as tk
from time import strftime
from datetime import datetime
import pytz

class WorldClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamic World Clock")
        self.root.geometry("500x600")
        
        # Timezones to display
        self.locations = {
            "Local Time": None,
            "New York": "America/New_York",
            "London": "Europe/London",
            "Tokyo": "Asia/Tokyo",
            "Mumbai": "Asia/Kolkata",
            "Sydney": "Australia/Sydney"
        }
        
        self.labels = {}
        self.setup_ui()
        self.update_time()

    def get_bg_color(self):
        hour = datetime.now().hour
        # Logic for soft light colors based on time of day
        if 5 <= hour < 12: return "#1ADBF5" # Morning: Soft Cyan
        if 12 <= hour < 17: return "#FF0116" # Afternoon: Pale Yellow
        if 17 <= hour < 20: return "#08FD00" # Evening: Peach
        return "#0077FF"                     # Night: Soft Lavender

    def setup_ui(self):
        self.container = tk.Frame(self.root, padx=20, pady=20)
        self.container.pack(expand=True, fill="both")
        
        for city in self.locations:
            city_label = tk.Label(self.container, text=city, font=("Helvetica", 14, "bold"))
            city_label.pack(pady=(10, 0))
            
            time_label = tk.Label(self.container, text="", font=("Courier", 24))
            time_label.pack(pady=(0, 10))
            
            self.labels[city] = time_label

    def update_time(self):
        current_bg = self.get_bg_color()
        self.root.config(bg=current_bg)
        self.container.config(bg=current_bg)
        
        for city, tz_name in self.locations.items():
            if tz_name:
                tz = pytz.timezone(tz_name)
                time_str = datetime.now(tz).strftime('%H:%M:%S\n%d %b %Y')
            else:
                time_str = datetime.now().strftime('%H:%M:%S\n%d %b %Y')
            
            self.labels[city].config(text=time_str, bg=current_bg, fg="#333333")
            # Update matching city labels too
            for child in self.container.winfo_children():
                if isinstance(child, tk.Label):
                    child.config(bg=current_bg)

        self.root.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    app = WorldClockApp(root)
    root.mainloop()
