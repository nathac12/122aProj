import csv
import os
def printNL2SQLresult():
    full_path = os.path.join(os.getcwd(), "nl2sql_results.csv")
    try:
        with open(full_path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(", ".join(str(col) for col in row))
    except FileNotFoundError:
        print("File not found.")

