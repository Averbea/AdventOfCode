'''
    Advent of code working directories creator
    IMPORTANT Remember to edit the USER_SESSION_ID & author values with yours
    uses requests module. If not present use pip install requests
    Author = Alexe Simon
    Date = 06/12/2018
 '''

import sys
import os

from config import *


try:
    import requests
except ImportError:
    sys.exit("You need requests module. Install it by running pip install requests.")

f = open(SESSION_ID_FILE, "r")
USER_SESSION_ID = f.read().strip()



'''
    creates URL icon in folder

'''
def create_url(folder, link_to_day):
    url = open(folder+"/link.url", "w+")
    url.write("[InternetShortcut]\nURL="+link_to_day+"\n")
    url.close()

def download_statements(folder, link_to_day):
    done = False
    error_count = 0
    while not done:
        try:
            with requests.get(url=link_to_day, cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}) as response:
                if response.ok:
                    html = response.text
                    start = html.find("<article")
                    end = html.rfind("</article>")+len("</article>")
                    end_success = html.rfind("</code>")+len("</code>")
                    statement = open(folder+"/statement.md", "w+")
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
    done = False
    error_count = 0
    while(not done):
        try:
            with requests.get(url=day_link+"/input", cookies={"session": USER_SESSION_ID}, headers={"User-Agent": USER_AGENT}) as response:
                if response.ok:
                    data = response.text
                    input = open(folder+"/input.txt", "w+")
                    input.write(data.rstrip("\n"))
                    input.close()
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
        except Exception as e:
            print("        Non handled error while requesting input from server. " + str(e))
            done = True


def make_code_template(folder, year, day, author, date):
    code = open(folder+"/solution.py", "w+")
    code.write("from time import time\n# Advent of code Year "+str(year)+" Day "+str(day)+" solution\n# Author = "+author+"\n# Date = "+date+"\n\nstart = time()\n\nwith open((__file__.rstrip(\"solution.py\")+\"input.txt\"), 'r') as input_file:\n    input = input_file.read()\n\n\n\nprint(\"Part One : \"+ str(None))\n\n\n\nprint(\"Part Two : \"+ str(None))\n\nprint(\"time elapsed: \" + str(time() - start))")
    code.close()




def main():
    
    years = range(STARTING_ADVENT_OF_CODE_YEAR, LAST_ADVENT_OF_CODE_YEAR+1)
    days = range(1,26)
    BASE_LINK = "https://adventofcode.com/" # ex use : https://adventofcode.com/2017/day/19/input
    

    print("Setup will download data and create working directories and files for adventofcode.")
    if not os.path.exists(BASE_FOLDER):
        os.mkdir(BASE_FOLDER)
    for y in years:
        print("Year "+str(y))
        if not os.path.exists(BASE_FOLDER+str(y)):
            os.mkdir(BASE_FOLDER+str(y))
        YEAR_FOLDER = BASE_FOLDER + str(y)
        for d in (d for d in days if (y < LAST_ADVENT_OF_CODE_YEAR or d <= LAST_ADVENT_OF_CODE_DAY)):
            print("    Day "+str(d))
            
            link_to_day = BASE_LINK + str(y) + "/day/" + str(d)

            if not os.path.exists(YEAR_FOLDER+"/"+str(d)):
                os.mkdir(YEAR_FOLDER+"/"+str(d))
            DAY_FOLDER = YEAR_FOLDER+"/"+str(d)
            if MAKE_CODE_TEMPLATE and not os.path.exists(DAY_FOLDER+"/solution.py"):
                make_code_template(DAY_FOLDER, y, d, AUTHOR, DATE)
            if DOWNLOAD_INPUTS and (not os.path.exists(DAY_FOLDER+"/input.txt") or OVERWRITE)and USER_SESSION_ID != "":
                download_inputs(DAY_FOLDER, link_to_day)
            if DOWNLOAD_STATEMENTS and (not os.path.exists(DAY_FOLDER+"/statement.md") or OVERWRITE):
                download_statements(DAY_FOLDER, link_to_day)
            if MAKE_URL and (not os.path.exists(DAY_FOLDER+"/link.url") or OVERWRITE):
                create_url(DAY_FOLDER, link_to_day)
    print("Setup complete : adventofcode working directories and files initialized with success.")


if __name__ == "__main__":
    # Code
    main()
