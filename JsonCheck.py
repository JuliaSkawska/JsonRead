import json
def CheckResource(filename):
    with open(filename, 'r') as inp:
        data = json.load(inp)
    try:
        resource = data['PolicyDocument']['Statement'][0]['Resource']
        if resource == '*':
            return True
        else:
            return False
    except (KeyError, IndexError):
        error_message = f"Error: File '{filename}' does not contain 'Resource'"
        return error_message

print(CheckResource('test.json'))