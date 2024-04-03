# JsonCheck:

Allows users to iterate over files inside a directory to check JSON files for the presence of "Resource" containing only "*".

## Installation:

1. Clone or download the repository
2. Install dependencies: None, project uses only standar python library

## Usage:

1. Create a directory containing files for testing.\
   
  For Bash:\
2. Run the program from the console: `$python JsonCheck.py`\
\
  For Powershell:\
2. Enter the catalogue in which JsonCheck is contained using cd, then run the program 'python JsonCheck.py'

3. Enter the path to the directory created in step 1 when prompted.
4. The program will return a list containing True (if "Resource" contains only "*"), False (if the condition is not met), or an error message with information on what went wrong for each file tested.

### Example:
Bash\
$ python JsonCheck.py\
Enter a path to catalogue containing JSON files for testing: /path/to/directory/json
\
\
Powershell\
cd /path/to/directory
python JsonCheck.py\
Enter a path to catalogue containing JSON files for testing: /path/to/directory/json


## Features:

- Checking for "Resource" containing only "*".
- Handling of edge cases.
- Providing information on possible errors.
- Includes a "Test" directory containing examples for testing the program.

## Additional:

To possibly expand the project, more file type coverage could be added as well as the possibility to manipulate which element of the JSON file is being checked and for what (depending on the user's needs)
