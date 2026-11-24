"""Robot pickup line entry for make.fun's The Robot Pickup Line Championship.

Writes exactly one pickup line, spoken by a robot, to /output/entry.txt.
Standard library only.
"""

import os

LINE = (
    "I don't have a heart, I have a gyroscope \u2014 and ever since "
    "you walked in, it's been spinning off-balance."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
