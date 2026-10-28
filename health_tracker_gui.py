# Health Tracker - Simple Interface
# A window version of health_tracker.py, built with tkinter (it comes with Python)

import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

# Same file the text version uses, so both share your history
DATA_FILE = "health_log.csv"


def get_feedback(water, sleep, calories):
    """Return a list of feedback messages for today's numbers."""
    messages = []

    if water >= 8:
        messages.append("Great job staying hydrated!")
    else:
        messages.append("Try to drink more water!")

    if sleep >= 7:
        messages.append("Good sleep schedule!")
    else:
        messages.append("Try to get more rest!")

    # Calorie needs are different for everyone, so these are just rough ranges
    if calories < 1200:
        messages.append("That might not be enough fuel for your body today.")
    elif calories > 3000:
        messages.append("That's a lot of calories - check if it matches your activity level.")
    else:
        messages.append("Your calories are in a typical range.")

    return messages


def save_entry(water, sleep, calories):
    """Add today's entry to the CSV file."""
    # If the file doesn't exist yet, we need to write the header row first
    file_exists = os.path.exists(DATA_FILE)

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["date", "water", "sleep", "calories"])
        writer.writerow([date.today(), water, sleep, calories])


def load_entries():
    """Read every saved entry. Returns an empty list if nothing is saved yet."""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def show_history():
    """Fill the history table and update the averages."""
    # Clear the old rows first
    for row in history_table.get_children():
        history_table.delete(row)

    entries = load_entries()

    for entry in entries:
        history_table.insert("", "end", values=(
            entry["date"], entry["water"], entry["sleep"], entry["calories"]
        ))

    if len(entries) == 0:
        averages_label.config(text="No days tracked yet.")
        return

    total_water = 0
    total_sleep = 0
    total_calories = 0
    for entry in entries:
        total_water += int(entry["water"])
        total_sleep += float(entry["sleep"])
        total_calories += int(entry["calories"])

    days = len(entries)
    averages_label.config(text=(
        f"Days tracked: {days}   |   "
        f"Avg water: {total_water / days:.1f} cups   |   "
        f"Avg sleep: {total_sleep / days:.1f} hours   |   "
        f"Avg calories: {total_calories / days:.0f}"
    ))


def on_save():
    """Runs when the Save Today button is clicked."""
    # try/except catches it if someone types letters instead of numbers
    try:
        water = int(water_entry.get())
        sleep = float(sleep_entry.get())
        calories = int(calories_entry.get())
    except ValueError:
        messagebox.showerror(
            "Oops!",
            "Please enter numbers only.\n\n"
            "Water and calories should be whole numbers (like 8 or 2000).\n"
            "Sleep can have a decimal (like 7.5)."
        )
        return

    save_entry(water, sleep, calories)

    feedback = get_feedback(water, sleep, calories)
    feedback_label.config(text="\n".join(feedback))

    # Clear the boxes for next time
    water_entry.delete(0, "end")
    sleep_entry.delete(0, "end")
    calories_entry.delete(0, "end")

    show_history()


# ---------- Build the window ----------

window = tk.Tk()
window.title("Daily Health Tracker")
window.geometry("620x520")

main = ttk.Frame(window, padding=20)
main.pack(fill="both", expand=True)

title_label = ttk.Label(main, text="Daily Health Tracker", font=("Helvetica", 20, "bold"))
title_label.pack(pady=(0, 15))

# Input boxes
form = ttk.Frame(main)
form.pack()

ttk.Label(form, text="Cups of water:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
water_entry = ttk.Entry(form, width=12)
water_entry.grid(row=0, column=1, pady=5)

ttk.Label(form, text="Hours of sleep:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
sleep_entry = ttk.Entry(form, width=12)
sleep_entry.grid(row=1, column=1, pady=5)

ttk.Label(form, text="Calories eaten:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
calories_entry = ttk.Entry(form, width=12)
calories_entry.grid(row=2, column=1, pady=5)

save_button = ttk.Button(main, text="Save Today", command=on_save)
save_button.pack(pady=10)

# Feedback area
feedback_label = ttk.Label(main, text="Enter today's numbers and click Save Today.", justify="center")
feedback_label.pack(pady=(0, 15))

# History table
ttk.Label(main, text="Your History", font=("Helvetica", 14, "bold")).pack(anchor="w")

columns = ("date", "water", "sleep", "calories")
history_table = ttk.Treeview(main, columns=columns, show="headings", height=8)
history_table.heading("date", text="Date")
history_table.heading("water", text="Water (cups)")
history_table.heading("sleep", text="Sleep (hours)")
history_table.heading("calories", text="Calories")
for column in columns:
    history_table.column(column, anchor="center", width=130)
history_table.pack(fill="both", expand=True, pady=5)

averages_label = ttk.Label(main, text="")
averages_label.pack(pady=(5, 0))

# Show any saved history when the window opens
show_history()

# Pressing Enter also saves
window.bind("<Return>", lambda event: on_save())

water_entry.focus()
window.mainloop()
