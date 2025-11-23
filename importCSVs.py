import os
import csv

def import_data(folderName : str):
    if folderName == "NULL" :
        folderName = None

    print("Importing from:", folderName)


    try:
        # DROP TABLEs
        # CREATE TABLEs

        # Read CSV(s) from folder
        folder_path = os.path.join(os.getcwd(), folderName)

        if not os.path.isdir(folder_path):
            print("Folder not found")
            print("Failed")
            return False

        for filename in os.listdir(folder_path):

            # only check for CSVs
            if not filename.endswith(".csv"):
                continue

            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r", newline = "") as file:
                reader = csv.DictReader(file)

                for row in reader:
                    print("Row: ", row) # replace this with SQL stuff

        # if Exception, return false
        # if no Exception, return true

        print("Success") # False: "Fail". True: "Success"
        return True

    except Exception as e:
        print("Error:", e)
        print("Fail")
        return False

