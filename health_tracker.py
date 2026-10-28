# Simple Health Tracker

import csv
import os
from datetime import date

# File where each day's entry is saved
DATA_FILE = "health_log.csv"

print("Welcome to your Daily Health Tracker!")

# Get user input
water = int(input("How many cups of water did you drink today? "))
sleep = float(input("How many hours did you sleep? "))
calories = int(input("About how many calories did you eat today? "))

# Feedback
print("\n--- Daily Summary ---")
print(f"Water intake: {water} cups")
print(f"Sleep: {sleep} hours")
print(f"Calories: {calories}")

# Simple health feedback
if water >= 8:
    print("Great job staying hydrated!")
else:
    print("Try to drink more water!")

if sleep >= 7:
    print("Good sleep schedule!")
else:
    print("Try to get more rest!")

# Calorie needs are different for everyone, so these are just rough ranges
if calories < 1200:
    print("That might not be enough fuel for your body today.")
elif calories > 3000:
    print("That's a lot of calories - check if it matches your activity level.")
else:
    print("Your calories are in a typical range.")

# Save today's entry
# If the file doesn't exist yet, we need to write the header row first
file_exists = os.path.exists(DATA_FILE)

with open(DATA_FILE, "a", newline="") as file:
    writer = csv.writer(file)
    if not file_exists:
        writer.writerow(["date", "water", "sleep", "calories"])
    writer.writerow([date.today(), water, sleep, calories])

print(f"\nToday's entry was saved to {DATA_FILE}.")

# Read all saved entries to show your history
with open(DATA_FILE, newline="") as file:
    reader = csv.DictReader(file)
    entries = list(reader)

print("\n--- Your History ---")
for entry in entries:
    print(f"{entry['date']}: {entry['water']} cups, {entry['sleep']} hours, {entry['calories']} calories")

# Averages across every saved day
total_water = 0
total_sleep = 0
total_calories = 0
for entry in entries:
    total_water += int(entry["water"])
    total_sleep += float(entry["sleep"])
    total_calories += int(entry["calories"])

days = len(entries)
print(f"\nDays tracked: {days}")
print(f"Average water: {total_water / days:.1f} cups")
print(f"Average sleep: {total_sleep / days:.1f} hours")
print(f"Average calories: {total_calories / days:.0f}")

print("\nKeep taking care of your health!")
