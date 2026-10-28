# Health Tracker (Python)

This is a beginner Python project that tracks daily health habits such as water intake, sleep, and calories.

## Features

- Tracks water consumption
- Tracks sleep hours
- Tracks calories
- Simple health feedback
- Saves each day's entry to `health_log.csv`
- Shows your history and average water, sleep, and calories
- Simple window interface with a history table (`health_tracker_gui.py`)

## How to Run

1. Make sure you have [Python 3](https://www.python.org/downloads/) installed.
2. Download or clone this project.
3. Open a terminal in the project folder and run:

```bash
python3 health_tracker.py
```

4. Answer the questions about how much water you drank, how long you slept, and about how many calories you ate.

### Window version

To use the simple interface instead, run:

```bash
python3 health_tracker_gui.py
```

Type your numbers into the boxes and click **Save Today** (or press Enter). Your feedback appears under the button, and the table shows every saved day with your averages underneath. If you type something that isn't a number, a pop-up asks you to fix it.

Both versions save to the same `health_log.csv`, so your history is shared between them.

## Example Output

```
Welcome to your Daily Health Tracker!
How many cups of water did you drink today? 6
How many hours did you sleep? 8
About how many calories did you eat today? 2000

--- Daily Summary ---
Water intake: 6 cups
Sleep: 8.0 hours
Calories: 2000
Try to drink more water!
Good sleep schedule!
Your calories are in a typical range.

Today's entry was saved to health_log.csv.

--- Your History ---
2026-10-27: 9 cups, 6.5 hours, 2200 calories
2026-10-28: 6 cups, 8.0 hours, 2000 calories

Days tracked: 2
Average water: 7.5 cups
Average sleep: 7.2 hours
Average calories: 2100

Keep taking care of your health!
```

## How It Works

- **Water:** 8 or more cups gets a "Great job staying hydrated!" message. Fewer than 8 suggests drinking more water.
- **Sleep:** 7 or more hours gets a "Good sleep schedule!" message. Fewer than 7 suggests getting more rest.
- **Calories:** Under 1200 suggests you might not have eaten enough, over 3000 suggests checking it against your activity level, and anything in between is a typical range. Everyone's needs are different, so these are just rough guides.
- **Saving:** Each run adds a row (date, water, sleep, calories) to `health_log.csv`. The file is created the first time you run the program, and you can open it in Excel or Google Sheets.

## What I Learned

- Python basics (input/output, variables)
- Conditional statements (if/else)
- Connecting coding with health concepts
- Reading and writing files with the `csv` module
- Using loops to calculate averages
- Using `elif` to check more than two options
- Building a window interface with `tkinter`
- Writing functions to organize code
- Using `try/except` to handle bad input

## Future Improvements

- ~~Save data over time~~ Done!
- ~~Add calorie tracking~~  Done!
- ~~Create a simple interface~~  Done!
- Keep only one entry per day
- Show charts of progress over time
