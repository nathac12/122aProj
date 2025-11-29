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
    print(args)
    funcName = args[FUNCINDEX]

    dataBase = initDB()
    myCursor = dataBase.cursor()
    myCursor.execute("USE cs122a")

    # no need to check args length
    match funcName:
        case "import":
            importTables.initTables(myCursor)
            folderName = args[2]
            importTables.load_csv(folderName, myCursor, dataBase)
        case "insertAgentClient":
            command.insertAgentClient(args[2:], myCursor, dataBase)
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


