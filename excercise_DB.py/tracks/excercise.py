import sqlite3

conn = sqlite3.connect('exercise_emaildb.sqlite')
cur = conn.cursor()

CREATE TABLE Artist(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)

CREATE TABLE Genre(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
)

CREATE TABLE Album(
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
)

CREATE TABLE Track(
    id  INTEGER NOT NULL PRIMARY KEY
    AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
)
fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    # person_and_org = email.split('@')
    # print(person_and_org)
    org = email.split('@')[1]
    # print(org)
    # ? va a ser csev@umich.edu o lo que sea, el ? es un marcador de posicion
    # email, es una tupla con una sola cosa
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:  # si no encuentro con el select el email
        #     # agrego el email y pongo un uno recoredar que ? es la posicion
        cur.execute(
            'INSERT INTO Counts (org, count) VALUES (?, 1)', (org,))
    else:
        # si encuentro el email sumop uno
        cur.execute(
            'UPDATE  Counts SET count = count + 1 WHERE org = ?', (org,))

conn.commit()
sqlstr = 'SELECT org, count FROM Counts  ORDER BY count DESC LIMIT 10'
for row in cur.execute(sqlstr):
    print(row[0], row[1])
cur.close()
