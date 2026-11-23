"""AKA Lab-6"""

import subprocess
import os
import time

if __name__ == "__main__":
    print("--- Select start range ---")
    min = input("Select MIN value for vector range: ")
    max = input("Select MAX value for vector range: ")

    if not min or not max:
        min, max = 0, 1

    subprocess_vector_creator = subprocess.Popen(
        [
            "python",
            "./submodules/submodule_vector_creator.py",
            "-min", str(min),
            "-max", str(max)
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    time.sleep(1)
    subprocess_vector_receiver = subprocess.Popen(
        ["python", "./submodules/submodule_vector_receiver.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    try:
        while True:
            print("--- Update vector range ('exit' for quit) ---")
            min = input(f"MIN value: ")
            if min == "exit":
                break
            max = input(f"MAX value: ")
            if max == "exit":
                break

            subprocess_vector_creator.stdin.write(f"{min} {max}\n".encode())
            subprocess_vector_creator.stdin.flush()
            time.sleep(1)
            subprocess_vector_receiver.stdin.write(f"refresh\n".encode())
            subprocess_vector_receiver.stdin.flush()

            print(f"Communicated. \n")
    finally:
        subprocess_vector_creator.kill()
        subprocess_vector_receiver.kill()