from database import db

def runQuery(q):
    try:
        cursor = db.cursor()
        cursor.execute(q)
        if q.strip().upper().startswith("INSERT") or q.strip().upper().startswith("UPDATE") or q.strip().upper().startswith("DELETE"):
            db.commit()
            rows = cursor.fetchall()
            cursor.close()
            return rows
        elif q.strip().upper().startswith("SELECT"):
            rows = cursor.fetchall()
            cursor.close()
            return rows
        return []
    except Exception as e:
        print("Error executing Query  : "+q)
        print(e)

def checkForValidLoginAdmin(email,password):
    rows = runQuery(f"SELECT id FROM ADMIN WHERE email='{email}' AND password='{password}'")
    if(rows==None or len(rows)==0):
        return False
    else:
        return rows[0]

def checkForValidLoginUser(email,password):
    rows = runQuery(f"SELECT id FROM USER WHERE email='{email}' AND password='{password}'")
    if(rows==None or len(rows)==0):
        return False
    else:
        return rows[0]

def getUserDetails():
    rows = runQuery(f"SELECT * FROM USER")
    users = []
    for row in rows:
        users.append({
            'id': row[0],    
            'email': row[1],     
            'password': row[2],
            'role': row[3],
            'status' : row[4] 
        })
    return users

def userExists(email):
    rows_user = runQuery(f"SELECT email FROM USER WHERE email='{email}'")
    rows_admin = runQuery(f"SELECT email FROM ADMIN WHERE email='{email}'")
    
    if (rows_user is not None and len(rows_user) > 0) or (rows_admin is not None and len(rows_admin) > 0):
        return True
    else:
        return False

def createUser(email,password):
    if userExists(email):
        return False
    runQuery(f"INSERT INTO USER(email,password) VALUES('{email}','{password}')")
    rows = runQuery(f"SELECT id FROM USER WHERE EMAIL='{email}'")
    if rows == None:
        return False
    return rows[0]

def updatePasswordAdmin(email,password):
    res = runQuery(f"UPDATE ADMIN SET password = '{password}' WHERE email = '{email}'")
    if res:
        return True
    else:
        return False

def updatePasswordUser(email,password):
    res = runQuery(f"UPDATE USER SET password = '{password}' WHERE email = '{email}'")
    if res:
        return True
    else:
        return False

def updatePassword(email,password):
    if userExists(email):
        if updatePasswordAdmin(email,password):
            return True
        elif updatePasswordUser(email,password):
            return True
        else:
            return False
    else:
        return False

def getAdminIndividualDetail(email):
    row = runQuery(f"SELECT * FROM ADMIN WHERE EMAIL ='{email}'")
    return row

def getUserIndividualDetail(email):
    row = runQuery(f"SELECT * FROM USER WHERE EMAIL ='{email}' AND status = 'active'")
    return row if row else False

def updateUser(id,email,password,role,status):
    runQuery(f"UPDATE USER SET email = '{email}', password = '{password}', role = '{role}', status = '{status}' WHERE id = '{id}'")
    return True

def addAdmin(email,password):
    runQuery(f"INSERT INTO ADMIN (email, password) VALUES('{email}','{password}')")
    return True

def removeUser(id):
    runQuery(f"DELETE FROM USER WHERE id = '{id}'")
    return True

def addUser(email,password,role):
    runQuery(f"INSERT INTO USER(email,password,role) VALUES('{email}','{password}','{role}')")
    return True

def addAdmin(email,password):
    runQuery(f"INSERT INTO ADMIN(email,password) VALUES('{email}','{password}')")
    return True

def deleteUser(id):
    runQuery(f"DELETE FROM USER WHERE id = '{id}'")
    return True