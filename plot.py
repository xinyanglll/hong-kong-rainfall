"""
Read the rainfall file in data/, make one picture, save it to out/.

Run:
uv run plot.py
"""

# /// script
# dependencies = [
#   "matplotlib",
# ]
# ///

import csv
from pathlib import Path

import matplotlib.pyplot as plt

FILE = "hko-daily-total-rainfall-2026.csv"
PICTURE = "hong-kong-rainfall.png"

HERE = Path(__file__).parent
DATA = HERE / "data" / FILE
OUT = HERE / "out"


def rows(path):
    """Read the rainfall CSV and keep only rows beginning with a year."""
    kept = []

    with path.open(encoding="utf-8-sig", newline="") as handle:
        for line in csv.reader(handle):
            if line and line[0].isdigit():
                kept.append(line)

    return kept


def main():
    table = rows(DATA)

    print(f"{DATA.name}: {len(table)} rows.")
    print(f"The first row: {table[0]}")
    print(f"One value: {table[0][3]}")
    print(f"Type: {type(table[0][3])}")
    
    days = []
    values = []

    for i, (year, month, day, value, quality) in enumerate(table):
        if value in ("***", "Trace"):
            continue

        days.append(i + 1)
        values.append(float(value))

    print(f"{len(values)} rainfall values")
    print(f"from {min(values)} to {max(values)} mm")

    fig, ax = plt.subplots(figsize=(10, 4))

    ax.plot(days, values, linewidth=1.5)

    ax.set_xlabel("day of 2026")
    ax.set_ylabel("daily rainfall (mm)")
    ax.set_title("Hong Kong Observatory — Daily Rainfall in 2026")

    fig.tight_layout()

    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / PICTURE, dpi=150)

    print(f"saved out/{PICTURE}")

    plt.show()


if __name__ == "__main__":
    main()