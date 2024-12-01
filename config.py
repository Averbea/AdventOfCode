'''
    Configurations
'''

#### General Settings
SESSION_ID_FILE = "UserSessionId.txt"

# Folders will be created here.
# # If you want to make a parent folder, change this to ex "./adventofcode/"
BASE_FOLDER = "./"


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
MAKE_URL = False

# Name automatically put in the code templates.
AUTHOR = "Averbea"

# If you really need to download the whole thing again, set this to true.
# As the creator said, AoC is fragile; please be gentle.
# Statements and Inputs do not change. This will not overwrite codes.
OVERWRITE = True



USER_AGENT = "adventofcode_working_directories_creator"
MAX_RECONNECT_ATTEMPT = 2
