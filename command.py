def insertAgentClient(args, myCursor, dataBase):
    uid, username, email, cardnum, cardholder, exp, cvv, zip_code, interests = args
    try:
        myCursor.execute(
            "INSERT INTO AgentClient(uid, interests, cardholder, expire, cardno, cvv, zip) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (uid, interests, cardholder, exp, cardnum, cvv, zip_code)
        )
        dataBase.commit()
        return True

    except Exception as e:
        #print(e)
        return False
    
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
        #print(e)
        return False
    
def deleteBaseModel(args, myCursor, dataBase):
    # Check if BaseModel exists
    bmid = args[0]
    myCursor.execute("SELECT 1 FROM BaseModel WHERE bmid = %s", (bmid,))
    if myCursor.fetchone() is None:
        #print("cant find")
        return False  # no such model

    try:
        myCursor.execute("DELETE FROM BaseModel WHERE bmid = %s", (bmid,))
        dataBase.commit()
        return True
    except Exception as e: 
        #print(e)
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

    return myresult


def countCustomizedModel(args, myCursor, dataBase):

    bmids = sorted(int(x) for x in args)

    if not bmids:
        return []

    placeholders = ", ".join(["%s"] * len(bmids)) # a lot of "%s, %s, ..."

    sql = f"""
        SELECT M.bmid, B.description, COUNT(*)
        FROM CustomizedModel as M
        JOIN BaseModel B ON M.bmid = B.bmid
        WHERE M.bmid IN ({placeholders})
        GROUP BY M.bmid, B.description
        ORDER BY M.bmid ASC
        """

    myCursor.execute(sql, bmids)
    return myCursor.fetchall()

def topNLongestDurationConfiguration(args, myCursor, dataBase):

    uid = args[0]
    N = args[1]

    sql = f"""
        SELECT C.client_uid, C.cid, C.labels, C.content, MAX(MC.duration) AS maxDuration
        FROM Configuration C
        JOIN ModelConfigurations MC ON C.cid = MC.cid
        WHERE C.client_uid = %s
        GROUP BY C.cid
        ORDER BY maxDuration DESC
        LIMIT {N}
    """

    myCursor.execute(sql, (uid, ))
    return myCursor.fetchall()

def listBaseModelKeyWord(args, myCursor, dataBase):

    keyword = "%" + args[0] + "%"
    selectNum = 5

    sql = f"""
        SELECT M.bmid, I.sid,I.provider,L.domain
        FROM ModelServices M
        JOIN InternetService I ON M.sid = I.sid
        JOIN LLMService L ON I.sid = L.sid
        WHERE L.domain LIKE %s
        ORDER BY M.bmid ASC
        LIMIT {selectNum}
    """

    myCursor.execute(sql, (keyword,))
    return myCursor.fetchall()

def printNL2SQLresult(myCursor, dataBase):


