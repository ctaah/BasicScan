import os
import colorama
from colorama import Fore, Style
import shutil

colorama.init(autoreset=True)


def scan_for_items(directory, user_input):
    found_locations = []
    print(
        Fore.LIGHTRED_EX
        + Style.BRIGHT
        + f"Scanning for anything related to '{user_input}'... Please wait patiently!\n"
    )

    for root, dirs, files in os.walk(directory, topdown=True):
        for name in files + dirs:
            if user_input.lower() in name.lower():
                found_locations.append(os.path.join(root, name))
                print(Fore.LIGHTRED_EX + f"Found: {os.path.join(root, name)}")

    return found_locations


def delete_items(found_locations):
    while True:
        choice = (
            input(Fore.LIGHTRED_EX + "\nDo you want to delete all found items? (Y/N): ")
            .strip()
            .lower()
        )
        if choice == "y":
            for path in found_locations:
                try:
                    if os.path.isfile(path):
                        os.remove(path)
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                    print(Fore.LIGHTRED_EX + f"Deleted: {path}")
                except Exception as e:
                    print(Fore.LIGHTRED_EX + f"Error deleting {path}: {e}")
            break
        elif choice == "n":
            print(Fore.LIGHTRED_EX + "No files were deleted.")
            break
        else:
            print(Fore.LIGHTRED_EX + "Please enter 'Y' or 'N'.")


def main():
    user_input = input(Fore.LIGHTRED_EX + "Enter the object you want to search for: ")
    root_directory = "C:\\"
    results = scan_for_items(root_directory, user_input)

    if results:
        print(
            Fore.LIGHTRED_EX
            + Style.BRIGHT
            + f"\nScan complete! Found {len(results)} items related to '{user_input}'."
        )
        delete_items(results)
    else:
        print(
            Fore.LIGHTRED_EX
            + Style.BRIGHT
            + f"\nScan complete! No items related to '{user_input}' found."
        )
    input(Fore.LIGHTRED_EX + "\nPress Enter to exit...")


if __name__ == "__main__":
    main()
