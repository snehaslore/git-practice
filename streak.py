import os

# File to store streak count
file_name = "streak_count.txt"

# Check if file exists
if os.path.exists(file_name):
    with open(file_name, "r") as f:
        count = int(f.read())
else:
    count = 0

# Ask user if they did their task today
done = input("Did you complete your task today? (y/n): ").lower()

if done == "y":
    count += 1
    print(f"Great! Your current streak is: {count}")
else:
    count = 0
    print("No worries! Streak reset to 0.")

# Save the streak
with open(file_name, "w") as f:
    f.write(str(count))

##OUTPUT:
Did you complete your task today? (y/n): y
Great! Your current streak is: 1
