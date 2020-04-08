import sqlite3
from os import getcwd
import pprint

class DbInterface:
    def __init__(self, path):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def clear_parts(self):
        sql = 'DELETE FROM Parts'
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("Table was deleted succesfully")
        except sqlite3.IntegrityError:
            print("ERROR deleting")

    def set_part(self, node, code, photos, name, needs, confirm, prod, source):
        sql = 'INSERT INTO Parts \
                (node, code, photos, name, needs, confirm, prod, source)\
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
        args = [node, code, photos, name, needs, confirm, prod, source]
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
            print(f"{code} was succesfully setted")
        except sqlite3.IntegrityError:
            print(f"Error while setting the part {code}")
            self.conn.commit()

    def get_parts(self, node):
        sql = 'SELECT * from Parts WHERE node = ?'
        args = [node]
        try:
            self.cursor.execute(sql, args)
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Error while getting parts from {node} node")
        parts = self.cursor.fetchall()
        
        box = []
        for part in parts:
            photos = part[2].split("&") if part[2] else None
            box.append(
                {
                    "node":   part[0], 
                    "code":   part[1], 
                    "photos": photos, 
                    "name":   part[3], 
                    "needs":  part[4], 
                    "confirm":part[5], 
                    "prod":   part[6], 
                    "source": part[7],
                    "gd": part[8]
                }
            )

        return box


path = getcwd() + "/app/pandemia.db"
DB = DbInterface(path)
# parts = DB.get_parts(1)

# pp = pprint.PrettyPrinter()
# pp.pprint(parts[0])