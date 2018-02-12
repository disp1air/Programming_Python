from initdata import db
import pickle

dbfile = open('people-pickle', 'wb')   # в 3.X следует использовать двоичный режим работы с файлами,
pickle.dump(db, dbfile)                # т.к. данные имеют тип bytes, а не str
dbfile.close()
