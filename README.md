# FUTURE_CS_03
# Password Manager

A Python-based command-line tool to securely save and retrieve passwords.

## Features
- Save passwords securely with encryption.
- Retrieve passwords for any service.
- Stores data locally in an encrypted JSON file.

## Installation

1. Clone the repository:
   
   git clone https://github.com/Kisuvilu/FUTURE_CS_03.git
   cd password_manager
   

2. Install dependencies:
   
   pip install -r requirements.txt
   

## Usage

1. Run the program:

   python password_manager.py
   

2. Follow the menu to save or retrieve passwords:
   - Option 1: Save a new password.
   - Option 2: Retrieve a password.
   - Option 3: Exit the program.

## File Structure

password_manager/
├── key.key               # Encryption key
├── passwords.json        # Encrypted password storage
├── password_manager.py   # Main Python script
├── requirements.txt      # Dependencies
└── README.md             # Documentation


## Security Notes

- The `key.key` file is essential for encrypting and decrypting passwords. Keep it secure.
- Losing `key.key` will make all passwords unrecoverable.
- The `passwords.json` file contains encrypted passwords. Do not share it without the encryption key.

## Dependencies

This project requires the following Python library:
- `cryptography` (Install with "pip install cryptography")

## Future Enhancements

- Add a master password to protect access.
- Include a password generator.
- Use a database (e.g., SQLite) for password storage.
- Implement a graphical user interface (GUI).


### License
This project is open-source and available under the MIT License.
