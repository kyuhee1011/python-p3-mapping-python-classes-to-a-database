from config import CONN, CURSOR

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album
    @classmethod
    def create_table(cls):
        sql="""    CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            )
        """
        CURSOR.execute(sql)
     # ... rest of Song methods

    def save(self):
        sql = """
            INSERT INTO songs (name, album)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.album))
        CONN.commit()

#SQL query to grab the value of the id column of the last inserted row, 
# and set that equal to the given song instance's id attribute
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM songs").fetchone()[0]

        #create a new Song instance and save it.
    @classmethod
    def create(cls, name, album):
        song = Song(name, album)
        song.save()
        return song
    #The return value of create() should always be the object that we created.