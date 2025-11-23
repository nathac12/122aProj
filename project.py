import mysql.connector
import sys

import importCSVs

FUNCINDEX = 1
USER = "root"
PASSWORD = ""
def initDB():
    if PASSWORD == "" or USER == "":
        print("set your USER and PASSWORD!")
        return

    mydb = mysql.connector.connect(
        #edpost said to format it like this
        host="localhost",
        user=USER,
        password=PASSWORD
    )
    return mydb

def main():
    args = sys.argv
    funcName = args[FUNCINDEX]
    dataBase = initDB()
    # no need to check args length
    match funcName:
        case "import":
            # args([FUNCINDEX + 1]) : folderName (str)
            return importCSVs.import_data(args[FUNCINDEX + 1])
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



