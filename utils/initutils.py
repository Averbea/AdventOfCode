import concurrent.futures
import os
import shutil
import requests
from datetime import datetime
from config import *


f = open(SESSION_ID_FILE, "r", encoding="UTF-8")
USER_SESSION_ID = f.read().strip()


def create_url(folder: str, link_to_day: str):
    """creates an url icon

    Args:
        folder (str): folder to create icon in
        link_to_day (str): url for link
    """
    with open(folder + "/link.url", "w+", encoding="UTF-8") as url:
        url.write("[InternetShortcut]\nURL=" + link_to_day + "\n")
        url.close()


def download_statements(folder: str, link_to_day: str):
    """downloads the task statement

    Args:
        folder (str): folder to download statement to
        link_to_day (str): url to day task
    """
    done = False
    error_count = 0
    while not done:
        try:
            with requests.get(url=link_to_day, cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT},
                              timeout=10) as response:
                if response.ok:
                    html = response.text
                    start = html.find("<article")
                    end = html.rfind("</article>") + len("</article>")
                    end_success = html.rfind("</code>") + len("</code>")
                    with open(folder + "/statement.md", "w+", encoding="UTF-8") as statement:
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
        except Exception as exc:
            print("        Non handled error while requesting statement from server. " + str(exc))
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
            with requests.get(url=day_link + "/input", cookies={"session": USER_SESSION_ID},
                              headers={"User-Agent": USER_AGENT}, timeout=10) as response:
                if response.ok:
                    data = response.text
                    with open(folder + "/input.txt", "w+", encoding="UTF-8") as input_file:
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


def prepend_line(file_name, line):
    """ Insert given string as a new line at the beginning of a file """
    # define name of temporary dummy file
    dummy_file = file_name + '.bak'
    # open original file in read mode and dummy file in write mode
    with open(file_name, 'r', encoding="utf-8") as read_obj, open(dummy_file, 'w', encoding="utf-8") as write_obj:
        # Write given line to the dummy file
        write_obj.write(line + '\n')
        # Read lines from original file one by one and append them to the dummy file
        for line in read_obj:
            write_obj.write(line)
    # remove original file
    os.remove(file_name)
    # Rename dummy file as the original file
    os.rename(dummy_file, file_name)


def make_code_template(folder, year, day, author, date):
    """creates a coding template from (uses template.py)

    Args:
        folder (str): folder to create the template in
        year (): year for this task
        day (): day for this task
        author (str): author of the code
        date (): Date description in code template
    """

    shutil.copy("./template.py", folder + "solution.py")
    docstring = '""" Advent of code Year ' + str(year) + ' Day ' + str(day) + ' solution\n'
    docstring += 'Link to task: https://adventofcode.com/' + str(year) + '/day/' + str(day) + '\n'
    docstring += 'Author = ' + author + '\n'
    docstring += 'Date = ' + date + '\n"""\n\n'
    prepend_line(folder + "solution.py", docstring)


def init_day(d, y):
    base_link = "https://adventofcode.com/"  # ex use : https://adventofcode.com/2017/day/19/input

    link_to_day = base_link + str(y) + "/day/" + str(d)
    day_folder = BASE_FOLDER + str(y) + "/" + str(d) + "/"
    if not os.path.exists(day_folder):
        os.makedirs(day_folder)

    if MAKE_CODE_TEMPLATE and not os.path.exists(day_folder + "/solution.py"):
        make_code_template(day_folder, y, d, AUTHOR, datetime.now().strftime("%d/%m/%Y"))
    if DOWNLOAD_INPUTS and (not os.path.exists(day_folder + "/input.txt") or OVERWRITE) and USER_SESSION_ID != "":
        download_inputs(day_folder, link_to_day)
    if DOWNLOAD_STATEMENTS and (not os.path.exists(day_folder + "/statement.md") or OVERWRITE):
        download_statements(day_folder, link_to_day)
    if MAKE_URL and (not os.path.exists(day_folder + "/link.url") or OVERWRITE):
        create_url(day_folder, link_to_day)

def init_multiple(start_year, last_year, start_day, last_day):
    """
    downloads all tasks and inputs from start_year/start_day to last_year/last_day
    """
    years = range(start_year, last_year+1)
    days = range(start_day,last_day + 1)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for y in years:
            for d in (d for d in days if (y < last_year or d <= last_day)):
                print("Initializing day " + str(d) + " of year " + str(y))
                futures.append(executor.submit(init_day, d, y))

        concurrent.futures.wait(futures)
        # exceptions
        for idx, future in enumerate(futures):
            if future.exception() is not None:
                print("Error while initializing day "+str(idx))
                print('\t'+str(future.exception()))