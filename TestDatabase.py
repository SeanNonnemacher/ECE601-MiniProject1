from TwitterDBConnector import MyDB

myDB = MyDB()

try:
    print(myDB.search_word('light'))
    
except Exception as e:
    print(e)


myDB.close_connection()