import csv

def printNL2SQLresult():
    try:
        with open("nl2sql_results.csv", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(", ".join(str(col) for col in row))
    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    printNL2SQLresult()