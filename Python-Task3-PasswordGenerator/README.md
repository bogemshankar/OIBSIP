# Random Password Generator

A command-line Python tool that generates strong random passwords based on user-selected criteria.

## Features
- Choose password length (minimum 8 characters)
- Choose character types: uppercase, lowercase, numbers, symbols (at least 2 required)
- Guarantees at least one character from every selected type
- Input validation for invalid length and invalid choices
- Generate another password without restarting the program

## How to Run
```
python password_generator.py
```

## Password Rules
| Rule | Details |
|------|---------|
| Minimum length | 8 characters |
| Character types | At least 2 must be selected |
| Invalid input | Rejected with a message and asked again |

## Example Output
![Output](Password_Output.png)

## Tech Used
- Python
- random module
- string module
