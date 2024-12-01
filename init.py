'''
    Advent of code working directories creator
    IMPORTANT Remember to edit the USER_SESSION_ID & author values with yours
    uses requests module. If not present use pip install requests
    Author = Alexe Simon
    Date = 06/12/2018
 '''
from dateutil.utils import today

from utils.initutils import init_day, init_multiple
import datetime

def main():

    today = datetime.date.today()
    default_year = today.year
    default_day = today.day


    multiple = bool(input("Do you want to initialize all days and years? [y/n] [n]: ").lower() == "y")
    if multiple:
        start_year = int(input(f"Enter start year [2015]: ") or 2015)
        last_year = int(input(f"Enter last year [{default_year}]: ") or default_year)
        start_day = int(input(f"Enter start day [1]: ") or 1)
        last_day = int(input(f"Enter last day [25]: ") or 25)
        init_multiple(start_year, last_year, start_day, last_day)
    else:

        year = int(input(f"Enter year [{default_year}]: ") or default_year)
        day = int(input(f"Enter day [{default_day}]: ") or default_day)

        year = int(year)
        day = int(day)

        init_day(day, year)

    print("Setup complete")


if __name__ == "__main__":
    main()
