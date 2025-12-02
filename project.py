import mysql.connector
import sys
import importTables
import command
FUNCINDEX = 1
USER = "root"
PASSWORD = ""
def initDB():
    mydb = mysql.connector.connect(
        #edpost said to format it like this, this is what they will run on the autograder
        #make sure to run the queries in ed post #251 on your local mysql server to create the database
        #https://edstem.org/us/courses/88195/discussion/7345549
        host="localhost",
        user="test",
        password="password"
    )
    return mydb

def main():
    args = sys.argv
    print(f"[TEST] args: {args}")
    funcName = args[FUNCINDEX]
    data = args[2:]
    dataBase = initDB()
    myCursor = dataBase.cursor()
    myCursor.execute("USE cs122a")


    # no need to check args length
    match funcName:
        case "import":
            importTables.initTables(myCursor)
            folderName = args[2]

            result = importTables.load_csv(folderName, myCursor, dataBase)
            printIsSuccess(result)
        case "insertAgentClient":
            result = command.insertAgentClient(data, myCursor, dataBase)
            printIsSuccess(result)
        case "addCustomizedModel":
            result = command.addCustomizedModel(data, myCursor, dataBase)
            printIsSuccess(result)
        case "deleteBaseModel":
            result = command.deleteBaseModel(data, myCursor, dataBase)
            printIsSuccess(result)
        case "listInternetService":
            result = command.listInternetService(data, myCursor, dataBase)
            printTable(result)
        case "countCustomizedModel":
            return 0
        case "topNDurationConfig":
            return 0
        case " listBaseModelKeyWord":
            return 0
        case _:
            print("wrong function name")
            return -1


def printIsSuccess(isSuccess : bool):
    if isSuccess:
        print("Success")
    else:
        print("Fail")

def printTable(rows : list[tuple]):
    for row in rows:
        line = ",".join(str(value) for value in row)
        print(line)



if __name__ == "__main__":
    main()


