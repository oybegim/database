import sqlite3 as sql

a = sql.connect("odamlar.db")



b = a.cursor()

b.execute("""
CREATE TABLE IF NOT EXISTS Studentlar(
    stu TEXT,
    prog TEXT, 
    bek TEXT
)
""")

b.execute("""
CREATE TABLE IF NOT EXISTS Folbinlar(
    ism TEXT,
    yosh INTEGER, 
    fam TEXT
)
""")

b.execute("""
CREATE TABLE IF NOT EXISTS Dasturchilar(
    xy TEXT,
    ab INTEGER, 
    op TEXT
)
""")

