from database import db

def runQuery(q):
    try:
        cursor = db.cursor()
        cursor.execute(q)
        if q.strip().upper().startswith("INSERT") or q.strip().upper().startswith("UPDATE") or q.strip().upper().startswith("DELETE") or q.strip().upper().startswith("CREATE"):
            db.commit()
            rows = cursor.fetchall()
            cursor.close()
            return rows
        elif q.strip().upper().startswith("SELECT") or q.strip().upper().startswith("DROP"):
            rows = cursor.fetchall()
            cursor.close()
            return rows
        return []
    except Exception as e:
        print("Error executing Query  : "+q)
        print(e)

def f():
    

    runQuery(
    """
    CREATE TABLE IF NOT EXISTS ADMIN(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        email varchar(50) UNIQUE,
        password varchar(50) NOT NULL
    )
    """)

    runQuery(
    """
    CREATE TABLE IF NOT EXISTS USER(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        email varchar(50) UNIQUE,
        password varchar(50) NOT NULL,
        role VARCHAR(50) DEFAULT 'users' NOT NULL
        status VARCHAR(50) DEFAULT 'active' NOT NULL
    )
    """)

    runQuery(
    """
        INSERT INTO ADMIN (email, password) 
        VALUES 
            ('admin.com', 'ab123')
        ON DUPLICATE KEY UPDATE 
            email = VALUES(email), 
            password = VALUES(password)
    """)

f()

