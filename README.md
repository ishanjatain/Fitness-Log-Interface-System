# Fitness-Log-Interface-System
A lightweight, console-based application written in Python for tracking daily physical activities and calculating total calories burned. This script uses simple Object-Oriented Programming (OOP) principles to manage activity records efficiently.

# Features
Activity Logging: Record the name, duration (in minutes), and calories burned for any physical activity.

Data Validation: Basic error handling to ensure minutes and calories are stored as valid numbers, defaulting to zero if input is invalid.

Total Calorie Count: Quickly calculate and display the cumulative total of calories burned from all recorded activities.

Simple Visualization: Provides a basic hash-tag bar visualization of the total calories burned (scaled by 50).

Easy Navigation: Simple command-line menu for interaction.

# Installation
1. Clone the Repository (or download the file):
git clone https://github.com/YourUsername/Simple-Fitness-CLI-Tracker.git
cd Simple-Fitness-CLI-Tracker
2. Prerequisites: You only need Python 3 installed on your system.

# Usage
Execute the script directly from your terminal:
python your_script_name.py
(Note: Replace 'your_script_name.py' with the actual filename of your code)

# Example-Session
=== FITNESS TRACK MENU ===
1. Add Activity
2. Total Calories
3. Show All
9. Quit
Choose option: 1
Activity name: Running
Minutes spent: 30
Calories: 350
Date (YYYY-MM-DD): 2024-11-24
Added: 2024-11-24

=== FITNESS TRACK MENU ===
...
Choose option: 2
Total calories burned: 350
#######

=== FITNESS TRACK MENU ===
...
Choose option: 3
--- Records ---
Running for 30.0 minutes, 350 Kcal on 2024-11-24

# Contributing
Contributions are welcome! If you have ideas for improvements, such as adding data persistence (saving records to a file) or more advanced reporting, please feel free to:

1.Fork the repository.

2.Create a new branch (git checkout -b feature/improvement).

3.Commit your changes (git commit -am 'Add feature X').

4.Push to the branch (git push origin feature/improvement).

5.Create a new Pull Request.
