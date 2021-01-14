import argparse
from datetime import datetime
import time
import subprocess
import sys
import platform
""" Takes two arguments: user's desired class hour, and the class URL.
Checks every 30 mins if the current hour == requested hour, and opens their
class, method being dependent on which operating system they're using."""
flag = True


def create_parser():
    parse = argparse.ArgumentParser(
        description="Opens the user's class via URL at the specified hour"
    )
    parse.add_argument(
        "hour",
        help="Requested hour (24hr format) 0:00, 01:30, etc")
    parse.add_argument("URL", help="Class URL, e.g. https://zoom.us/j/1234567")
    return parse


def main(args):
    current_hour = datetime.now().strftime("%H:%M")
    operating_system = platform.system()
    parser = create_parser()
    user_info = parser.parse_args(args)

    global flag
    while flag:
        if user_info.hour == current_hour:
            print(f"It's now {user_info.hour}! Opening class...")
            if operating_system == "Darwin":
                subprocess.run(["open", user_info.URL])
            elif operating_system == "Linux":
                subprocess.run(["xdg-open", user_info.URL])
            elif operating_system == "Windows":
                subprocess.run(["start", user_info.URL])
            flag = False
        time.sleep(1800)


if __name__ == "__main__":
    main(sys.argv[1:])
