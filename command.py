def insertAgentClient(args, myCursor, dataBase):
    uid, username, email, cardnum, cardholder, exp, cvv, zip_code, interests = args

    myCursor.execute(
        "INSERT INTO User(uid, email, username) VALUES (%s, %s, %s)",
        (uid, email, username)
    )
    
    myCursor.execute(
        "INSERT INTO AgentClient(uid, interests, cardholder, expire, cardno, cvv, zip) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (uid, interests, cardholder, exp, cardnum, cvv, zip_code)
    )
    dataBase.commit()
