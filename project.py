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

def initTables(cursor):
    cursor.execute("DROP TABLE IF EXISTS ModelConfigurations")
    cursor.execute("DROP TABLE IF EXISTS ModelServices")
    cursor.execute("DROP TABLE IF EXISTS DataStorage")
    cursor.execute("DROP TABLE IF EXISTS LLMService")
    cursor.execute("DROP TABLE IF EXISTS InternetService")
    cursor.execute("DROP TABLE IF EXISTS Configuration")
    cursor.execute("DROP TABLE IF EXISTS CustomizedModel")
    cursor.execute("DROP TABLE IF EXISTS BaseModel")
    cursor.execute("DROP TABLE IF EXISTS AgentClient")
    cursor.execute("DROP TABLE IF EXISTS AgentCreator")
    cursor.execute("DROP TABLE IF EXISTS User")

    cursor.execute("CREATE TABLE User (uid INT,email TEXT NOT NULL,username TEXT NOT NULL,PRIMARY KEY (uid))")
    cursor.execute("CREATE TABLE AgentCreator (uid INT,bio TEXT,payout TEXT,PRIMARY KEY (uid),FOREIGN KEY (uid) REFERENCES User(uid) ON DELETE CASCADE)")
    cursor.execute("CREATE TABLE AgentClient (uid INT,interests TEXT NOT NULL,cardholder TEXT NOT NULL,expire DATE NOT NULL,cardno INT NOT NULL,cvv INT NOT NULL,zip INT NOT NULL,PRIMARY KEY (uid),FOREIGN KEY (uid) REFERENCES User(uid) ON DELETE CASCADE)")
    cursor.execute("CREATE TABLE BaseModel (bmid INT,creator_uid INT NOT NULL,description TEXT NOT NULL,PRIMARY KEY (bmid),FOREIGN KEY (creator_uid) REFERENCES AgentCreator(uid) ON DELETE CASCADE)")
    cursor.execute("CREATE TABLE CustomizedModel (bmid INT,mid INT NOT NULL,PRIMARY KEY (bmid, mid),FOREIGN KEY (bmid) REFERENCES BaseModel(bmid) ON DELETE CASCADE)")
    cursor.execute("CREATE TABLE Configuration (cid INT,client_uid INT NOT NULL,content TEXT NOT NULL,labels TEXT NOT NULL,PRIMARY KEY (cid),FOREIGN KEY (client_uid) REFERENCES AgentClient(uid) ON DELETE CASCADE)")
    cursor.execute("CREATE TABLE InternetService (sid INT,provider TEXT NOT NULL,endpoints TEXT NOT NULL,PRIMARY KEY (sid))")
    cursor.execute("CREATE TABLE LLMService (sid INT,domain TEXT,PRIMARY KEY (sid),FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE)")
    cursor.execute("CREATE TABLE DataStorage (sid INT,type TEXT,PRIMARY KEY (sid),FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE)")
    cursor.execute("CREATE TABLE ModelServices (bmid INT NOT NULL,sid INT NOT NULL,version INT NOT NULL,PRIMARY KEY (bmid, sid),FOREIGN KEY (bmid) REFERENCES BaseModel(bmid) ON DELETE CASCADE,FOREIGN KEY (sid) REFERENCES InternetService(sid) ON DELETE CASCADE)")
    cursor.execute("CREATE TABLE ModelConfigurations (bmid INT NOT NULL,mid INT NOT NULL,cid INT NOT NULL,duration INT NOT NULL,PRIMARY KEY (bmid, mid, cid),FOREIGN KEY (bmid, mid) REFERENCES CustomizedModel(bmid, mid) ON DELETE CASCADE,FOREIGN KEY (cid) REFERENCES Configuration(cid) ON DELETE CASCADE)")

def main():
    args = sys.argv
    funcName = args[FUNCINDEX]
    dataBase = initDB()
    print(dataBase)
    myCursor = dataBase.cursor()
    myCursor.execute("USE cs122a")
    initTables(myCursor)
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


