# Advent of Code 🎄
This repo contains my personnal answers to all of the problems proposed by [AdventOfCode](https://adventofcode.com/).
Most of it is missing and will be added as I complete them. You can check the commits or the list below to know which has been completed. I also propose to viewers to use init.py to copy this repo hierarchy and get down to coding themselves.
# Current Results


## Stats
![](https://img.shields.io/badge/2021%20total%20stars%20⭐-0-yellow)
&nbsp;&nbsp;
![](https://img.shields.io/badge/2021%20days%20completed-0-red)


![](https://img.shields.io/badge/2022%20total%20stars%20⭐-0-yellow)
&nbsp;&nbsp;
![](https://img.shields.io/badge/2022%20days%20completed-0-red)


<!--- advent_readme_stars table_2021 --->
## 2021 Results

| Day | Part 1 | Part 2 |
| :---: | :---: | :---: |
| [Day 1](https://adventofcode.com/2021/day/1) | ⭐ | ⭐ |
| [Day 2](https://adventofcode.com/2021/day/2) | ⭐ | ⭐ |
| [Day 3](https://adventofcode.com/2021/day/3) | ⭐ | ⭐ |
| [Day 4](https://adventofcode.com/2021/day/4) | ⭐ | ⭐ |
| [Day 5](https://adventofcode.com/2021/day/5) | ⭐ | ⭐ |
| [Day 6](https://adventofcode.com/2021/day/6) | ⭐ | ⭐ |
| [Day 7](https://adventofcode.com/2021/day/7) | ⭐ | ⭐ |
| [Day 8](https://adventofcode.com/2021/day/8) | ⭐ | ⭐ |
| [Day 9](https://adventofcode.com/2021/day/9) | ⭐ | ⭐ |
| [Day 10](https://adventofcode.com/2021/day/10) | ⭐ | ⭐ |
| [Day 11](https://adventofcode.com/2021/day/11) | ⭐ | ⭐ |
| [Day 12](https://adventofcode.com/2021/day/12) | ⭐ | ⭐ |
| [Day 13](https://adventofcode.com/2021/day/13) | ⭐ | ⭐ |
| [Day 14](https://adventofcode.com/2021/day/14) | ⭐ | ⭐ |
| [Day 15](https://adventofcode.com/2021/day/15) | ⭐ | ⭐ |
| [Day 16](https://adventofcode.com/2021/day/16) | ⭐ | ⭐ |
| [Day 17](https://adventofcode.com/2021/day/17) | ⭐ |   |
| [Day 20](https://adventofcode.com/2021/day/20) | ⭐ | ⭐ |
| [Day 21](https://adventofcode.com/2021/day/21) | ⭐ | ⭐ |
<!--- advent_readme_stars table_2021 ---> 

# Credits
The init.py was originally created by [AlexeSimon](https://github.com/AlexeSimon) and adapted by me
The original Version can be found in his own [repository](https://github.com/AlexeSimon/adventofcode)




## Copying the template

You can use `init.py`, `config.py`, `template.py` and `update.py` if you want to copy this repo template and answer the problems by yourself.
Its functionnalities include making directories, downloading statements, downloading inputs, making code templates and making url links.

# Using this repo as template

### Prerequisites
You need python3 and its module "requests" installed.
To install the module requests, use
```shell
pip install requests
```
### Usage
* Create a new folder.
* Download `init.py`, `config.py`, `template.py` and `update.py` and put them into the folder.
* Put your Session ID into a seperate file specified in config.py
* Change other user parameters in the config.py as desired.
* Change the date of the last advent of code year and day if needed.
* Run init.py from within the folder with
```shell
python init.py
```

When you finished the first part of the coding challenge, update.py can be used to refetch the statement. 
Open it, change the parameters to the desired date and run 

```shell
python update.py
```

### configuring the template
The code template can be modified by changing `template.py`
### Users Parameters
The only important parameter is your **SESSION_ID**, which has to be set correctly for the script to download your personnal problems input.
To recover your session:
* Go to [AdventOfCode](https://adventofcode.com/).
* Log in by any means (GitHub, Google, ...).
* Check for a cookie named **session**. This step depends on the browser used. It can be done through network inspection or, in advanced browser like Chrome, by simply clicking on the **View site information** button directly left of the url (shown as a padlock), then clicking **Cookies**.
* Copy this cookie content and paste it in a file specified in config.py
*  Other parameters are self explanatory.

## Running this repo code
Simply download the wanted solution folders.
Script can be run from a parent directory:
```shell
python 2018/2/solution.py
```
Or set current directory to wanted solution folder:
```shell
cd 2018/2
python solution.py
```
Please do not rename the *solution.py* nor the *input.txt* files, as both their names are hardcoded in the solutions.

