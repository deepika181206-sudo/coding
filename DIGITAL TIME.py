import tkinter as tk
from time import strftime

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Customize the clock display
clock_label = tk.Label(root, font=('Arial', 60), background='black', foreground='cyan')
clock_label.pack(anchor='center')

# Function to update time
def update_time():
    current_time = strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)  # Update every 1000ms (1 second)

# Start the clock
update_time()
root.mainloop()
