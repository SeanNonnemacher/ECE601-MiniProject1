import mysql.connector

class MyDB():
    
    
    def __init__(self):
        self.my_db = mysql.connector.connect(
                host = "127.0.0.1",
                port = "3306",
                user = "root",
                password = "PASSWORD",
                database = "mydb"
        )    
        self.my_cursor = self.my_db.cursor()
        
        
    #Diconnects from database
    def close_connection(self):
        self.my_db.disconnect()
        
    
    #Adds new session and returns SessionID
    def add_new_session(self, twitter, numPics, numLabels):
        self.my_cursor.execute("""
            INSERT INTO sessions (TwitterHandle, NumPics, NumLabels)
            VALUES (%s, %s, %s)
        """, (twitter, numPics, numLabels))
        self.my_cursor.execute("""
            SELECT LAST_INSERT_ID()
            """)
        result = self.my_cursor.fetchone()[0]
        self.my_db.commit()
        return result
    
    
    #Adds new label for given session
    def add_new_label(self, sessionID, label):
        self.my_cursor.execute("""
            INSERT INTO labels (SessionID, Label)
            VALUES (%s, %s)
        """, (sessionID, label))
        self.my_db.commit()
        
        
    #Returns list of Sessions and Twitter containing word
    def search_word(self, word):
        result = []
        self.my_cursor.execute("""
            SELECT SessionID
            FROM labels
            WHERE Label = '%s'
        """ %(word))
        IDs = self.my_cursor.fetchall()
        for id in IDs:
            self.my_cursor.execute("""
                SELECT TwitterHandle
                FROM sessions
                WHERE SessionID = %d
            """ %(id[0]))
            result.append((self.my_cursor.fetchall()[0][0], id[0]))
        return result
    
    
        