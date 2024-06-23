import tkinter as tk

# Function to be called when the button is clicked
def button_click():
    label.config(text="Button Clicked!")

# Create the main window
window = tk.Tk()
window.title("Tkinter Example")

# Create a label
label = tk.Label(window, text="Hello, Tkinter!", font=("Arial", 18))
label.pack(pady=20)  # Add padding around the label

# Create a button
button = tk.Button(window, text="Click Me", command=button_click, font=("Arial", 14))
button.pack()

items = ["Option 1", "Option 2", "Option 3", "Option 4"]
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE)  # Or tk.SINGLE for single selection
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(pady=10)

# Start the GUI event loop
window.mainloop()
