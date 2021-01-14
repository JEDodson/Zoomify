from datetime import datetime
import time
import subprocess
import platform


def main():
    requested_hour = input("What time do you want to join your class (24hr): ")
    requested_class = input("What class do you want to join? Zoom URL: ")
    current_hour = datetime.now().strftime("%H")
    operating_system = platform.system()
    while True:
        if requested_hour == current_hour:
            if operating_system == "Darwin":
                subprocess.run(["open", requested_class])
                print(f"It's now {requested_hour}! Opening Zoom class...")
            elif operating_system == "Linux":
                subprocess.run(["xdg-open", requested_class])
                print(f"It's now {requested_hour}! Opening Zoom class...")
            elif operating_system == "Windows":
                subprocess.run(["start", requested_class])
                print(f"It's now {requested_hour}! Opening Zoom class...")
        time.sleep(3600)


if __name__ == "__main__":
    main()
