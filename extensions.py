import MySQLdb
import MySQLdb.cursors
import config

def connect_to_database():
  options = {
    'host': 0.0.0.0,
    'user': 'root',
    'passwd': 'root',
    'db': 'mhacks',
    'cursorclass' : MySQLdb.cursors.DictCursor
  }
  db = MySQLdb.connect(**options)
  db.autocommit(True)
  return db

db = connect_to_database()
