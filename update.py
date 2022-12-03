'''
downloads statements for year and day. Useful for getting part 2
'''

from init import os, download_statements
from config import BASE_FOLDER

YEAR = 2022
DAY = 2
DAY_FOLDER  = BASE_FOLDER + str(YEAR) + "/" + str(DAY) + "/"
if not os.path.exists(DAY_FOLDER):
    os.makedirs(DAY_FOLDER)

DAY_LINK = "https://adventofcode.com/" + str(YEAR) + "/day/" + str(DAY)
download_statements(DAY_FOLDER, DAY_LINK)
