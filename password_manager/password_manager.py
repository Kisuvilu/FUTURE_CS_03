import os
import base64
import json
from cryptography.fernet import Fernet

# Generate or load the encryption key
def load_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    else:
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
    return key

def encrypt_password(password, key):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()

def save_password(service, username, password):
    key = load_key()
    encrypted_password = encrypt_password(password, key)

    data = {}
    if os.path.exists('passwords.json'):
        with open('passwords.json', 'r') as file:
            data = json.load(file)

    data[service] = {'username': username, 'password': encrypted_password}

    with open('passwords.json', 'w') as file:
        json.dump(data, file, indent=4)

def retrieve_password(service):
    key = load_key()
    if not os.path.exists('passwords.json'):
        print("No passwords saved yet!")
        return

    with open('passwords.json', 'r') as file:
        data = json.load(file)

    if service in data:
        username = data[service]['username']
        encrypted_password = data[service]['password']
        password = decrypt_password(encrypted_password, key)
        print(f"Service: {service}\nUsername: {username}\nPassword: {password}")
    else:
        print(f"No password found for {service}.")

def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Save a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            service = input("Enter the service name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            save_password(service, username, password)
            print("Password saved successfully!")

        elif choice == '2':
            service = input("Enter the service name: ")
            retrieve_password(service)

        elif choice == '3':
            print("Exiting Password Manager. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
