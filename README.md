# Password Strength Assessment Tool 

## Overview
This **Password Strength Assessment Tool** is designed to evaluate the strength of a password and provide feedback on how secure it is. It analyzes various aspects of the password, such as its length, the inclusion of uppercase and lowercase letters, numbers, and special characters, and then offers suggestions to improve the overall security of the password.

## Features
- **Password Length Validation**: Ensures the password is at least 8 characters long, with additional points for passwords longer than 12 characters.
- **Uppercase and Lowercase Validation**: Checks if the password includes both uppercase and lowercase letters for enhanced strength.
- **Numeric Validation**: Validates if the password includes at least one numeric digit.
- **Special Character Validation**: Validates if the password includes at least one special character (such as `!@#$%^&*`).
- **Detailed Feedback**: Provides user-friendly feedback on what makes the password strong or weak and offers suggestions to improve it.

## How It Works
1. The user enters a password.
2. The tool evaluates the password on the following criteria:
   - **Length**: Passwords shorter than 8 characters are considered weak. Passwords with 12 or more characters are rewarded.
   - **Character Types**: The tool checks for the presence of uppercase, lowercase, numbers, and special characters.
   - **Strength Scoring**: Based on the checks above, the password is rated on a scale from weak to very strong.
3. Feedback is displayed to the user, detailing the password's strengths and weaknesses.

## Installation
1. Install **Python** (version 3.6 or above).
2. No external libraries are needed, but the tool uses Python's built-in `re` (Regular Expression) module for pattern matching.

## Usage
1. Clone the repository or copy the script into a Python environment.
2. Run the script and follow the on-screen prompts:
   ```bash
   python password_strength_tool.py
   ```
3. Enter the password you want to assess.
4. Review the feedback and suggestions for improving your password strength.

## Example
```
Enter your password: Hello123!
Password length is good.
Good: Password contains both uppercase and lowercase letters.
Good: Password contains numbers.
Good: Password contains special characters.
Password is very strong.
```

## Contributing
Feel free to fork the project and submit pull requests for improvements. Any contributions to enhance functionality or add new features are welcome!

## License
This project is licensed under the MIT License.

## Disclaimer
This tool is intended for educational and personal use. Ensure you follow best practices for password creation and security.
