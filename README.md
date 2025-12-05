# Advent of Code 🎄

This repo contains my personal answers to problems proposed by [AdventOfCode](https://adventofcode.com/).
Most of it is missing and will be added as I complete them.

## Current Results / Stats

![](https://img.shields.io/badge/2021%20total%20stars%20⭐-39-yellow)
&nbsp;&nbsp;
![](https://img.shields.io/badge/2021%20days%20completed-19-red)

![](https://img.shields.io/badge/2022%20total%20stars%20⭐-48-yellow)
&nbsp;&nbsp;
![](https://img.shields.io/badge/2022%20days%20completed-23-red)

![](https://img.shields.io/badge/2023%20total%20stars%20⭐-47-yellow)
&nbsp;&nbsp;
![](https://img.shields.io/badge/2023%20days%20completed-22-red)

![](https://img.shields.io/badge/2024%20total%20stars%20⭐-42-yellow)
&nbsp;&nbsp;
![](https://img.shields.io/badge/2024%20days%20completed-21-red)


![](https://img.shields.io/badge/2025%20total%20stars%20⭐-10-yellow)
&nbsp;&nbsp;
![](https://img.shields.io/badge/2025%20days%20completed-5-red)
## Credits

The init.py was originally created by [AlexeSimon](https://github.com/AlexeSimon) and adapted by me
The original Version can be found in his own [repository](https://github.com/AlexeSimon/adventofcode)

## Using this repo as template

### Prerequisites

You need python3 and its module "requests" installed.
To install the module requests, use

```shell
pip install requests
```

### Usage

* Create a new folder.
* Download `init.py`, `config.py`, `template.py` and the directory `utils` and put them into the folder.
* Put your Session ID into a seperate file specified in config.py (`UserSessionId.txt` by default)
* Change other user parameters in the config.py as desired.
* Run init.py from within the folder with

```shell
python init.py
```

When you finished the first part of the coding challenge, you can rerun `init.py` to refetch the statement.
`OVERWRITE` has to be set to `True` for this.

### Getting Sesision ID

To recover your session:

* Go to [AdventOfCode](https://adventofcode.com/).
* Log in by any means (GitHub, Google, ...).
* Check for a cookie named **session**. This step depends on the browser used. It can be done through network inspection
  or, in advanced browser like Chrome, by simply clicking on the **View site information** button directly left of the
  url (shown as a padlock), then clicking **Cookies**.
* Copy this cookie content and paste it in a file specified in config.py
* Other parameters are self explanatory.

### Configuring the template

The code template can be modified by changing `template.py`

## Running this repo code
Add the content root to your PYTHONPATH, to make the utils module available, or run in an IDE that does this for you.
