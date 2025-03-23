"""
Part 2: Adding decorators to handle input errors in a program. 
A simple bot assistant with CLI that manages contacts.
Supports adding, modifying, displaying and outputting contact list.
"""

# Декоратор для обробки помилок. Всі помилки уніфіковані та перенесені із самих функцій у декоратор.
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "No such contact in your list."
        except Exception as e:
            return f"Error: {e}"
    return inner


# Основний функціонал бота
def parse_input(user_input):                   # Тут обробка декоратором не потрібна, бо парсер лише передає дані далі на обробку функціям
    if not user_input.strip(): return "", []   # Якщо користувач натиснув лише Enter
    cmd, *args = user_input.strip().split()
    return cmd.lower(), args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name, = args
    return contacts[name]

@input_error
def show_all(contacts):
    if not contacts: 
        return "No contacts in your list."      # Якщо список ще порожній та повертається None
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

@input_error
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if not command: continue                # Якщо команда порожня, просто продовжуємо цикл
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()