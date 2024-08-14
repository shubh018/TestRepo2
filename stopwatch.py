import time
from datetime import datetime
# Track the amount of time elapsed between presses of the ENTER key, with each key press starting a new “lap” on the timer.
# Print the lap number, total time, and lap time.

i, results = 1, {}
first_lap = input("Press ENTER to start the first lap: ")
start_time = time.time()

while True:
    capture = input(f"Lap {str(i)} started, press ENTER to start a new lap and get info on the current lap (Enter SPACE to quit and get total result): ")

    if capture == " ":
        print("\n")
        print("Quitting Stopwatch, Printing Results...")
        time.sleep(2)
        print("\n")

        print("-----------------------------------")
        print("Laps", "\t\t", "Time (seconds)")
        for key, values in results.items():
            print(key, "------", values)

        print("-----------------------------------")

        print("\n")
        print("Stopwatch Stopped!")
        break

    if capture == '':
        print(f"Lap {str(i)} Ended\n Elapsed Time For This Lap:", str(time.time() - start_time))
        results.update({f"Lap {str(i)}": str(time.time() - start_time)})

    i += 1
