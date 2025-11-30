def insertAgentClient(args, myCursor, dataBase):
    uid, username, email, cardnum, cardholder, exp, cvv, zip_code, interests = args
    try:
        myCursor.execute(
            "INSERT INTO User(uid, email, username) VALUES (%s, %s, %s)",
            (uid, email, username)
        )
        
        myCursor.execute(
            "INSERT INTO AgentClient(uid, interests, cardholder, expire, cardno, cvv, zip) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (uid, interests, cardholder, exp, cardnum, cvv, zip_code)
        )
        dataBase.commit()
        return True
    except Exception as e: 
        print(e)
    

def addCustomizedModel(args, myCursor, dataBase):
    mid, bmid = args
    try:
        myCursor.execute(
            "INSERT INTO CustomizedModel(bmid, mid) VALUES (%s, %s)",
            (bmid, mid)
        )
        dataBase.commit()
        return True
    except Exception as e: 
        print(e)
        return False
    
def deleteBaseModel(args, myCursor, dataBase):
    # Check if BaseModel exists
    bmid = args[0]
    myCursor.execute("SELECT 1 FROM BaseModel WHERE bmid = %s", (bmid,))
    if myCursor.fetchone() is None:
        print("cant find")
        return False  # no such model

    try:
        myCursor.execute("DELETE FROM BaseModel WHERE bmid = %s", (bmid,))
        dataBase.commit()
        return True
    except Exception as e: 
        print(e)
        return False
    
def listInternetService(args, myCursor, dataBase):
    bmid = args[0]
    sql = """
        SELECT I.sid, I.endpoints, I.provider
        FROM InternetService I
        JOIN ModelServices as M on M.sid = I.sid
        WHERE M.bmid = %s
        ORDER BY I.provider ASC;
        """
    myCursor.execute(sql, (bmid,))
    myresult = myCursor.fetchall()
    for x in myresult:
        print(x)