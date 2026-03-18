# Simple Health Tracker

print("Welcome to your Daily Health Tracker!")

# Get user input
water = int(input("How many cups of water did you drink today? "))
sleep = float(input("How many hours did you sleep? "))

# Feedback
print("\n--- Daily Summary ---")
print(f"Water intake: {water} cups")
print(f"Sleep: {sleep} hours")

# Simple health feedback
if water >= 8:
    print("Great job staying hydrated!")
else:
    print("Try to drink more water!")

if sleep >= 7:
    print("Good sleep schedule!")
else:
    print("Try to get more rest!")

print("\nKeep taking care of your health!")
