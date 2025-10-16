import tkinter as tk
from tkinter import messagebox
import csv

# ==========================
# App Configuration
# ==========================
CSV_FILE = "expenses.csv"
FRAME_BG = 'lightblue'
BUTTON_BG = 'lightgray'
BUTTON_ACTIVE = 'red'
FONT_MONO = ("Courier", 12)

# ==========================
# Helper Functions
# ==========================
def load_expenses():
    """Load all expenses from CSV into a list"""
    expenses = []
    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:  # skip empty lines
                    expenses.append(row)
    except FileNotFoundError:
        pass
    return expenses

def save_expense(date, amount, place, utr):
    """Append a new expense to CSV"""
    try:
        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, amount, place, utr])
        messagebox.showinfo("Success", "Expense added!")
        e_amount.delete(0, tk.END)
        e_place.delete(0, tk.END)
        e_date.delete(0, tk.END)
        e_utr.delete(0, tk.END)
    except Exception as ex:
        messagebox.showerror("Error", f"Failed to save expense: {ex}")

def format_expenses(expenses_list):
    """Return a formatted string for display with aligned columns"""
    if not expenses_list:
        return "No expenses yet."
    
    headers = ["Date", "Item", "Amount", "UTR"]
    all_rows = [headers] + expenses_list
    col_widths = [max(len(str(row[i])) for row in all_rows)+2 for i in range(len(headers))]
    
    def format_row(row):
        return "".join(str(val).ljust(width) for val, width in zip(row, col_widths))
    
    lines = [format_row(headers)]
    lines.append("-"*sum(col_widths))
    
    total = 0
    for row in expenses_list:
        lines.append(format_row(row))
        try:
            total += float(row[1])
        except:
            pass  # skip if amount is not numeric
    
    lines.append("-"*sum(col_widths))
    lines.append(f"Total spent: {total}")
    return "\n".join(lines)

def switch_screen(target_frame):
    """Hide all frames and show target_frame"""
    for frame in frames:
        frame.pack_forget()
    target_frame.pack(fill="both", expand=True)

def add_expense_action():
    """Validate and save new expense"""
    date = e_date.get()
    place = e_place.get()
    utr = e_utr.get()
    try:
        amount = int(e_amount.get())
    except:
        messagebox.showerror("Invalid input", "Amount must be a number.")
        return
    save_expense(date, amount, place, utr)

def refresh_show_screen():
    """Reload expenses and update the show screen text"""
    all_expenses = load_expenses()
    show_text.config(state="normal")
    show_text.delete("1.0", tk.END)
    show_text.insert(tk.END, format_expenses(all_expenses))
    show_text.config(state="disabled")

def search_expenses():
    """Filter expenses based on search input"""
    query = search_entry.get().lower()
    filtered = [row for row in load_expenses() if query in " ".join(row).lower()]
    show_text.config(state="normal")
    show_text.delete("1.0", tk.END)
    show_text.insert(tk.END, format_expenses(filtered))
    show_text.config(state="disabled")

# ==========================
# Tkinter Setup
# ==========================
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("700x500")

# ==========================
# Frames
# ==========================
menu = tk.Frame(root, bg=FRAME_BG)
add_frame = tk.Frame(root, bg=FRAME_BG)
show_frame = tk.Frame(root, bg=FRAME_BG)

frames = [menu, add_frame, show_frame]

# ==========================
# Menu Screen
# ==========================
tk.Label(menu, text="Expense Tracker Menu", font=("Arial",16), bg=FRAME_BG).pack(pady=20)
tk.Button(menu, text="Add Expense", bg=BUTTON_BG, activebackground=BUTTON_ACTIVE,
          command=lambda: switch_screen(add_frame)).pack(pady=10)
tk.Button(menu, text="Review Expenses", bg=BUTTON_BG, activebackground=BUTTON_ACTIVE,
          command=lambda: [refresh_show_screen(), switch_screen(show_frame)]).pack(pady=10)

# ==========================
# Add Expense Screen
# ==========================
tk.Label(add_frame, text="Add a New Expense", font=("Arial",16), bg=FRAME_BG).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(add_frame, text="Amount:", bg=FRAME_BG).grid(row=1, column=0, sticky="e", padx=5, pady=5)
tk.Label(add_frame, text="Place:", bg=FRAME_BG).grid(row=2, column=0, sticky="e", padx=5, pady=5)
tk.Label(add_frame, text="Date (DD-MM-YYYY):", bg=FRAME_BG).grid(row=3, column=0, sticky="e", padx=5, pady=5)
tk.Label(add_frame, text="UTR:", bg=FRAME_BG).grid(row=4, column=0, sticky="e", padx=5, pady=5)

e_amount = tk.Entry(add_frame)
e_place = tk.Entry(add_frame)
e_date = tk.Entry(add_frame)
e_utr = tk.Entry(add_frame)

e_amount.grid(row=1, column=1, padx=5, pady=5)
e_place.grid(row=2, column=1, padx=5, pady=5)
e_date.grid(row=3, column=1, padx=5, pady=5)
e_utr.grid(row=4, column=1, padx=5, pady=5)

tk.Button(add_frame, text="Submit", bg=BUTTON_BG, activebackground="blue",
          command=add_expense_action).grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(add_frame, text="Back", bg=BUTTON_BG, activebackground=BUTTON_ACTIVE,
          command=lambda: switch_screen(menu)).grid(row=6, column=0, columnspan=2, pady=5)

# ==========================
# Show/Review Screen
# ==========================
tk.Label(show_frame, text="Expenses Review", font=("Arial",16), bg=FRAME_BG).pack(pady=10)

search_frame = tk.Frame(show_frame, bg=FRAME_BG)
search_frame.pack(pady=5)
tk.Label(search_frame, text="Search:", bg=FRAME_BG).pack(side="left")
search_entry = tk.Entry(search_frame)
search_entry.pack(side="left", padx=5)
tk.Button(search_frame, text="Go", command=search_expenses, bg=BUTTON_BG, activebackground="blue").pack(side="left")

show_text = tk.Text(show_frame, font=FONT_MONO)
show_text.pack(fill="both", expand=True, padx=10, pady=10)
show_text.config(state="disabled")

tk.Button(show_frame, text="Back to Menu", bg=BUTTON_BG, activebackground=BUTTON_ACTIVE,
          command=lambda: switch_screen(menu)).pack(pady=10)

# ==========================
# Start App
# ==========================
switch_screen(menu)
root.mainloop()
