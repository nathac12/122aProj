import os 
import csv

def load_csv(folderName: str, cursor, dataBase):
   #cant loop through the folder, we need to insert in a certain order due to relations
    folder_path = os.path.join(os.getcwd(), folderName)

    requiredCSVs = [
        "User.csv",
        "AgentCreator.csv",
        "AgentClient.csv",
        "BaseModel.csv",
        "CustomizedModel.csv",
        "Configuration.csv",
        "InternetService.csv",
        "LLMService.csv",
        "DataStorage.csv",
        "ModelServices.csv",
        "ModelConfigurations.csv"
    ]

    for filename in requiredCSVs:
       full_path = os.path.join(folder_path, filename)
       ok = parse_csv(full_path, filename, cursor, dataBase)

       if not ok:
            # missing file
           return False

    return True


def parse_csv(fileDir: str, fileName: str, cursor, dataBase):
    try:
        file = open(fileDir, newline="")
    except FileNotFoundError:
        return False

    fileName = fileName[:-4]

    with file:
        reader = csv.reader(file)
        header = next(reader)
        columns = ", ".join(header)
        placeholders = ", ".join(["%s"] * len(header))

        sql = f"INSERT INTO {fileName} ({columns}) VALUES ({placeholders})"
        rows = [row for row in reader]

        cursor.executemany(sql, rows)
        dataBase.commit()

    return True

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
