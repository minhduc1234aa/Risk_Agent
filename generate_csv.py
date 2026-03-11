#!/usr/bin/env python3
import csv
import argparse
import random
import sys


def generate_rows(n):
    for i in range(1, n + 1):
        yield {
            "id": i,
            "name": f"User{i}",
            "email": f"user{i}@example.com",
            "age": random.randint(18, 70),
        }


def write_csv(path, rows, headers):
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
    except OSError as e:
        print(f"Error writing file: {e}", file=sys.stderr)
        raise


def main():
    parser = argparse.ArgumentParser(description="Generate a sample CSV file.")
    parser.add_argument("-o", "--output", default="output.csv", help="Output CSV file path")
    parser.add_argument("-n", "--rows", type=int, default=10, help="Number of data rows to generate")
    args = parser.parse_args()

    headers = ["id", "name", "email", "age"]
    rows = generate_rows(args.rows)
    write_csv(args.output, rows, headers)
    print(f"Wrote {args.rows} rows to {args.output}")


if __name__ == "__main__":
    main()
