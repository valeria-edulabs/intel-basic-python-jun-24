import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI: {bmi:.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")

# Create main window
window = tk.Tk()
window.title("BMI Calculator")

# Weight Input
tk.Label(window, text="Weight (kg):").grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=5, pady=5)

# Height Input
tk.Label(window, text="Height (cm):").grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=5, pady=5)

# Calculate Button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

window.mainloop()
