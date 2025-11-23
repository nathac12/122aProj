import mysql.connector
import sys

FUNCINDEX = 1
def initDB():
    mydb = mysql.connector.connect(
        #edpost said to format it like this
        host="localhost",
        user="test",
        password="password"
    )
    return mydb

def main():
    args = sys.argv
    funcName = args[FUNCINDEX]
    dataBase = initDB()
    # no need to check args length
    match funcName:
        case "import":
            return 0
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



