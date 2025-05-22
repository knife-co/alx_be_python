# Create a file named future_age_calculator.py.
# Prompt the user to input their current age with the question: “How old are you? ”.
# Assume the user will input a valid integer value.
# Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
# Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.

# Expected Script Flow:

# The script prompts the user for their current age.
# The user enters their age.
# The script calculates and prints how old the user will be in 2050.

current_age = input(" How old are you ? ")
age = current_age + 27

print(f"In 2050, you will be {age} years old")
