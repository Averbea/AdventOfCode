'''
    Configurations
'''

## DATE SPECIFIC PARAMETERS

# Date automatically put in the code templates.
DATE = "December 2022"

# You can go as early as 2015.
STARTING_ADVENT_OF_CODE_YEAR = 2022

# The setup will download all advent of code data
# up until that date included
LAST_ADVENT_OF_CODE_YEAR = 2022

# If the year isn't finished, the setup will download days
# up until that day included for the last year
LAST_ADVENT_OF_CODE_DAY = 4


#### General Settings
SESSION_ID_FILE = "UserSessionId.txt"

# Folders will be created here.
# # If you want to make a parent folder, change this to ex "./adventofcode/"
BASE_FOLDER = "./"

# Set to false to download the whole range of tasks
ONLY_INIT_ONE_DAY = True

# Set to false to not download statements.
# Note that only part one is downloaded (since you need to complete it to access part two)
DOWNLOAD_STATEMENTS = True

# Set to false to not download inputs.
# Note that if the USER_SESSION_ID is wrong or left empty, inputs will not be downloaded.
DOWNLOAD_INPUTS = True

# Set to false to not make code templates.
# Note that even if OVERWRITE is set to True, it will never overwrite codes.
MAKE_CODE_TEMPLATE = True

# Set to false to not create a direct url link in the folder.
MAKE_URL = True

# Name automatically put in the code templates.
AUTHOR = "Averbea"

# If you really need to download the whole thing again, set this to true.
# As the creator said, AoC is fragile; please be gentle.
# Statements and Inputs do not change. This will not overwrite codes.
OVERWRITE = True



USER_AGENT = "adventofcode_working_directories_creator"
MAX_RECONNECT_ATTEMPT = 2
