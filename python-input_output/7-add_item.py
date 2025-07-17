#!/usr/bin/python3
"""
This script adds all command-line arguments to a Python list
and then saves them as a JSON representation to a file named 'add_item.json'.

It uses the save_to_json_file and load_from_json_file functions.
"""
import sys
import json

# --- Replicating 5-save_to_json_file.py content (assuming it uses json.dump) ---
def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a text file in JSON format.

    Args:
        my_obj: The Python object to be serialized.
        filename (str): The name of the file to save the JSON to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)

# --- Replicating 6-load_from_json_file.py content ---
def load_from_json_file(filename):
    """
    Creates a Python object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python object represented by the JSON content in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

# --- Main script logic ---
if __name__ == "__main__":
    filename = "add_item.json"
    current_list = []

    try:
        # Attempt to load the existing list from the file
        current_list = load_from_json_file(filename)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty list
        current_list = []
    except json.JSONDecodeError:
        # If the file exists but contains invalid JSON, start with an empty list
        # (This handles cases like an empty file or corrupted JSON)
        current_list = []

    # Add all command-line arguments (excluding the script name itself)
    # to the current list
    for arg in sys.argv[1:]:
        current_list.append(arg)

    # Save the updated list back to the file in JSON format
    save_to_json_file(current_list, filename)

    # Optional: Print the updated list to confirm (for testing purposes)
    # print(f"Updated list saved to {filename}: {current_list}")

