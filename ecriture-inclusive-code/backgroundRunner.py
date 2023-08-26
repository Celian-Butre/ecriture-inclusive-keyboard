PATH = "ecriture-inclusiveV2.py" #Replace with your path or keep this one if you leave both in the same folder

import subprocess
import time
import os
import signal

def run_program_for_duration(program_path, duration):
    # Start the program
    process = subprocess.Popen(["python3", program_path])

    # Run the program for the specified duration
    time.sleep(duration)

    # Kill the program
    os.kill(process.pid, signal.SIGTERM)
    process.wait()  # Wait for the process to terminate

if __name__ == "__main__":
    run_duration = 3600  # 1 hour in seconds

    try:
        while True:
            run_program_for_duration(PATH, run_duration)
    except KeyboardInterrupt:
        print("Execution stopped by user.")
