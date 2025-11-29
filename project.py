import mysql.connector
import sys
import importTables
FUNCINDEX = 1
USER = "root"
PASSWORD = ""
def initDB():
    if PASSWORD == "" or USER == "":
        print("set your USER and PASSWORD!")
        return

    mydb = mysql.connector.connect(
        #edpost said to format it like this, this is what they will run on the autograder
        #make sure to run the queries in ed post #251 on your local mysql server to create the database
        #https://edstem.org/us/courses/88195/discussion/7345549
        host="localhost",
        user=USER,
        password=PASSWORD
    )
    return mydb

def main():
    args = sys.argv
    funcName = args[FUNCINDEX]

    dataBase = initDB()
    myCursor = dataBase.cursor()
    myCursor.execute("USE cs122a")
    importTables.initTables(myCursor)

    # no need to check args length
    match funcName:
        case "import":
            folderName = args[2]
            importTables.load_csv(folderName, myCursor, dataBase)
        case "insertAgentClient":
            sql = f"INSERT into AgentClient (uid, interests, cardholder, expire, cardno, cvv, zip) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (args[2], args[3], args[4], args[5], args[6], args[7], args[8])
            myCursor.execute(sql, val)
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


