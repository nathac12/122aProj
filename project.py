import mysql.connector
import sys
import os 
import csv
FUNCINDEX = 1
def initDB():
    mydb = mysql.connector.connect(
        #edpost said to format it like this
        host="localhost",
        user="test",
        password="password"
    )
    return mydb

def get_dir(targetName: str):
    baseDir = os.path.dirname(os.path.abspath(__file__)) 
    csvDir = os.path.join(baseDir, "test_data_project_122a")
    for filename in os.listdir(csvDir):
        if targetName in filename:  
            print("Found:", filename)
            return os.path.join(csvDir, filename)
    print("file not found")
    return None

def parse_csv(fileDir: str, fileName: str, cursor, dataBase):
    file = open(fileDir, newline="")
    fileName = fileName[:-4]

    reader = csv.reader(file)
    header = next(reader)
    columns = ", ".join(header)
    placeholders = ", ".join(["%s"] * len(header))

    sql = f"INSERT INTO {fileName} ({columns}) VALUES ({placeholders})"
    rows = []
    for row in reader:
        rows.append(row) 

    val = rows
    cursor.executemany(sql, val)
    dataBase.commit()

def create_table(fileName: str, cursor):
    #creates a table, if one already exists delete the prev one 
    sql = f"DROP TABLE IF EXISTS {fileName}"
    cursor.execute(sql) 
    sql = f"CREATE TABLE {fileName}" #dont know how to do this right now
    cursor.execute(sql) 


def main():
    args = sys.argv
    funcName = args[FUNCINDEX]
    dataBase = initDB()
    myCursor = dataBase.cursor()
    # no need to check args length
    match funcName:
        case "import":
            fileName = args[2]
            parse_csv(get_dir(fileName), fileName, myCursor, dataBase)
        case "insertAgentClient":
            return 0
        case "addCustomizedModel":
            return 0
        case "deleteBaseModel":
            return 0
        case "listInternetService":
            return 0
        case "countCustomizedModel":
            return 0
        case "topNDurationConfig":
            return 0
        case " listBaseModelKeyWord":
            return 0
        case _:
            print("wrong function name")
            return -1


if __name__ == "__main__":
    main()


