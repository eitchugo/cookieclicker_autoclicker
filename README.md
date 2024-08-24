# Eitch's Cookie Clicker Autoclicker

This is a just for fun and learning project to have the computer automatically click on the cookie of the
game `Cookie Clicker`, also trying to click on the temporary golden cookies in the screen.

It's an external program and not a mod for the game. And it's just for fun, to click in this great idle
game while I sleep.

## Installing and developing

Tested only on Linux, with Python 3.12. Should work on other systems and versions, anyway.

Install it inside a `virtualenv` to make things easier:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

This installs using develop mode, so you can also edit files at will :)

The `cookieclicker_autoclicker` command should be installed in your virtual environment, so after
`sourcing`, the command should be available.

## Usage

In the terminal, you run

```bash
cookieclicker_autoclicker
```

It will wait 3 seconds and begin clicking.

There is two ways to stop the program:

- There's a 1-2 second gap between clicking intervals, so you can `CTRL+C` in the terminal to stop it.
- Also in this seconds gap, you can move the mouse to trigger the FailSafe from `PyAutoGUI`.

## Efficiency

This program is not efficient and doesn't have any goals to be the most good on it. For example, the golden cookie
recognizion is a bit unreliable and many golden cookies will be missed. There's also some gaps between click
intervals that I want to be on it.

Just reminding: this is just a for-fun project :)

Usually if you want efficiency and a lot of automation on cookie clicker, there's mods for the game that could
do everything for you. I don't want that, I only want the auto-clicking while I'm sleep. Other actions like
upgrading builds, play mini games, select upgrades, etc, I want to do it myself!

## Libraries/Dependencies used

- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) is the main library, used for easily clicking and
  taking screenshots for golden cookie detection.
- [Python Pillow](https://python-pillow.org/) is the library used by `PyAutoGUI` to take a screenshot and try
  to recognize a golden cookie on the screen based on sample images.
- [OpenCV Python](https://github.com/opencv/opencv-python) enables the `confidence` parameter to work while
  PyAutoGUI and Pillow tries to recognize the golden cookie.

## TODO

- Make argument parser for all options, like:
  - How many seconds to wait after running the program
  - Quantity of clicks, interval time
  - Images to compare with the golden cookie

- Have some more optimizations on Pillow/OpenCV to recognize the golden cookie better.

- Maybe instead of screenshotting and searching the whole screen, detect the Cookie Clicker window
  and only work on that area?

- Have a TUI to control and show clicking status, while being able to create a shortcut for starting and stoping.

- Maybe also A GUI?
