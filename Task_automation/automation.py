import re

try:
    with open("input.txt", "r") as f:
        text = f.read()
    # Regular expression specifically crafted to match email addresses:
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    with open("emails.txt", "w") as f:
        for email in emails:
            f.write(email + "\n")
    print(f"Extracted {len(emails)} email addresses and saved to emails.txt")
except FileNotFoundError:
    print("Error: 'input.txt' was not found.")
    print("Creating a sample 'input.txt' file for you. Please run the script again!")
    with open("input.txt", "w") as f:
        f.write("Welcome to the automation test.\nFeel free to contact support@example.com or admin@test.org for help!")