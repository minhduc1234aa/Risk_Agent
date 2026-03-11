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


