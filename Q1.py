# Currency Converter using Tkinter (Event Driven Programming)
import tkinter as tk
from tkinter import messagebox

# Currency conversion rates (example values)
RATE = {
    'USD': 1.0,
    'INR': 83.0,
    'EUR': 0.92,
    'GBP': 0.79,
    'JPY': 156.5
}

def convert():
    """Function to convert currency based on user input"""
    try:
        amt = float(amount.get())
        from_cur = from_currency.get()
        to_cur = to_currency.get()

        if from_cur not in RATE or to_cur not in RATE:
            messagebox.showerror("Error", "Invalid currency selected!")
            return

        # Convert amount
        result_val = amt * RATE[to_cur] / RATE[from_cur]
        result.set(f"{amt:.2f} {from_cur} = {result_val:.2f} {to_cur}")

    except ValueError:
        messagebox.showerror("Error", "Enter a valid numeric amount!")

# ------------------ GUI Design ------------------
root = tk.Tk()
root.title("Currency Converter")
root.geometry("350x250")

# Input variables
amount = tk.StringVar()
from_currency = tk.StringVar(value='USD')
to_currency = tk.StringVar(value='INR')
result = tk.StringVar()

# Labels and inputs
tk.Label(root, text="Amount:", font=('Arial', 10)).pack(pady=5)
tk.Entry(root, textvariable=amount, font=('Arial', 10)).pack(pady=5)

tk.Label(root, text="From Currency:", font=('Arial', 10)).pack(pady=5)
tk.OptionMenu(root, from_currency, *RATE.keys()).pack(pady=5)

tk.Label(root, text="To Currency:", font=('Arial', 10)).pack(pady=5)
tk.OptionMenu(root, to_currency, *RATE.keys()).pack(pady=5)

# Convert button
tk.Button(root, text="Convert", command=convert, bg="lightblue", font=('Arial', 10, 'bold')).pack(pady=10)

# Result label
tk.Label(root, textvariable=result, font=('Arial', 12, 'bold'), fg="green").pack(pady=10)

# Run the app
root.mainloop()
