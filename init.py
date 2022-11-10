'''
    Advent of code working directories creator
    IMPORTANT Remember to edit the USER_SESSION_ID & author values with yours
    uses requests module. If not present use pip install requests
    Author = Alexe Simon
    Date = 06/12/2018
 '''

import os
import sys

from config import *

try:
    import requests
except ImportError:
    sys.exit("You need requests module. Install it by running pip install requests.")

f = open(SESSION_ID_FILE, "r", encoding="UTF-8")
USER_SESSION_ID = f.read().strip()




def create_url(folder:str, link_to_day:str):
    """creates an url icon

    Args:
        folder (str): folder to create icon in
        link_to_day (str): url for link
    """
    with open(folder+"/link.url", "w+", encoding="UTF-8") as url:
        url.write("[InternetShortcut]\nURL="+link_to_day+"\n")
        url.close()

def download_statements(folder:str, link_to_day:str):
    """downloads the task statement

    Args:
        folder (str): folder to download statement to
        link_to_day (str): url to day task
    """
    done = False
    error_count = 0
    while not done:
        try:
            with requests.get(url=link_to_day, cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}, timeout={print("timeout")}) as response:
                if response.ok:
                    html = response.text
                    start = html.find("<article")
                    end = html.rfind("</article>")+len("</article>")
                    end_success = html.rfind("</code>")+len("</code>")
                    with open(folder+"/statement.md", "w+", encoding="UTF-8") as statement:
                        statement.write(html[start:max(end, end_success)])
                        statement.close()
                done = True
        except requests.exceptions.RequestException:
            error_count += 1
            if error_count > MAX_RECONNECT_ATTEMPT:
                print("        Error while requesting statement from server. Request probably timed out. Giving up.")
                done = True
            else:
                print("        Error while requesting statement from server. Request probably timed out. Trying again.")
        except Exception as e:
            print("        Non handled error while requesting statement from server. " + str(e))
            done = True


def download_inputs(folder, day_link):
    """download the inputs

    Args:
        folder (str): folder to download to
        day_link (str): url to day task
    """
    done = False
    error_count = 0
    while not done:
        try:
            with requests.get(url=day_link+"/input", cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}, timeout={print("timeout")}) as response:
                if response.ok:
                    data = response.text
                    with open(folder+"/input.txt", "w+", encoding="UTF-8") as input_file:
                        input_file.write(data.rstrip("\n"))
                        input_file.close()
                else:
                    print("        Server response for input is not valid.")
            done = True
        except requests.exceptions.RequestException:
            error_count += 1
            if error_count > MAX_RECONNECT_ATTEMPT:
                print("        Giving up.")
                done = True
            elif error_count == 0:
                print("        Error while requesting input from server. Request probably timed out. Trying again.")
            else:
                print("        Trying again.")
        except Exception as exception:
            print("        Non handled error while requesting input from server. " + str(exception))
            done = True


def make_code_template(folder, year, day, author, date):
    """creates a coding template

    Args:
        folder (str): folder to create the template in
        year (): year for this task
        day (): day for this task
        author (str): author of the code
        date (): Date description in code template
    """
    code = open(folder+"/solution.py", "w+", encoding="UTF-8")
    code.write("from time import time\n# Advent of code Year "+str(year)+" Day "+str(day)+" solution\n# Author = "+author+"\n# Date = "+date+"\n\nstart = time()\n\nwith open((__file__.rstrip(\"solution.py\")+\"input.txt\"), 'r') as input_file:\n    input = input_file.read()\n\n\n\nprint(\"Part One : \"+ str(None))\n\n\n\nprint(\"Part Two : \"+ str(None))\n\nprint(\"time elapsed: \" + str(time() - start))")
    code.close()




def main():
    """downloads all tasks and inputs according to config
    """
    years = range(STARTING_ADVENT_OF_CODE_YEAR, LAST_ADVENT_OF_CODE_YEAR+1)
    days = range(1,26)
    base_link = "https://adventofcode.com/" # ex use : https://adventofcode.com/2017/day/19/input


    print("Setup will download data and create working directories and files for adventofcode.")
    for y in years:
        print("Year "+str(y))

        for d in (d for d in days if (y < LAST_ADVENT_OF_CODE_YEAR or d <= LAST_ADVENT_OF_CODE_DAY)):
            print("    Day "+str(d))

            link_to_day = base_link + str(y) + "/day/" + str(d)
            day_folder  = BASE_FOLDER + str(y) + "/" + str(d) + "/"
            if not os.path.exists(day_folder):
                os.makedirs(day_folder)

            if MAKE_CODE_TEMPLATE and not os.path.exists(day_folder+"/solution.py"):
                make_code_template(day_folder, y, d, AUTHOR, DATE)
            if DOWNLOAD_INPUTS and (not os.path.exists(day_folder+"/input.txt") or OVERWRITE)and USER_SESSION_ID != "":
                download_inputs(day_folder, link_to_day)
            if DOWNLOAD_STATEMENTS and (not os.path.exists(day_folder+"/statement.md") or OVERWRITE):
                download_statements(day_folder, link_to_day)
            if MAKE_URL and (not os.path.exists(day_folder+"/link.url") or OVERWRITE):
                create_url(day_folder, link_to_day)
    print("Setup complete : adventofcode working directories and files initialized with success.")


if __name__ == "__main__":
    main()
