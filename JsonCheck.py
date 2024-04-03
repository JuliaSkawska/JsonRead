import os
import json
from json.decoder import JSONDecodeError


def FindResource(data):  #looks for instances of 'Resource' in JSON file and returns its value
    if isinstance(data, dict):
        for key, value in data.items():
            if key == 'Resource':
                return value
            elif isinstance(value, (dict, list)):
                result = FindResource(value)
                if result is not None:
                    return result
    elif isinstance(data, list):
        for elem in data:
            result = FindResource(elem)
            if result is not None:
                return result
    return None


def CheckResource(filename):  #Checks if Resource value is '*' and return errors if something is wrong with file
    try:
        with open(filename, 'r') as input_file:
            data = json.load(input_file)
    except JSONDecodeError:
        error_message1 = f"Error: File '{filename}' has invalid syntax or is empty"
        return error_message1
    except FileNotFoundError:
        error_message3 = f"Error: File '{filename}' was not found"
        return error_message3

    search=FindResource(data)

    if search == '*':
        return False
    elif search is None:
        error_message2 = f"Error: File '{filename}' does not contain 'Resource'"
        return error_message2
    else:
        return True


def RunCheck():  #Runs the code over multiple files
    directory=input("Enter a path to catalogue containing JSON files for testing:")
    runresult=[]
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' not found.")
        return
    if not os.listdir(directory):
        print(f"The directory '{directory}' is empty.")
        return
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            runresult.append(CheckResource(file_path))
    return runresult

RunCheck()
