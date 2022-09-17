import os
import sqlite3
import pandas as pd

# Clear example.db if it exists
if os.path.exists('univ.sqlite'):
    os.remove('univ.sqlite')

# Create a database
conn = sqlite3.connect('univ.sqlite', check_same_thread=False)

conn.execute('''DROP TABLE IF EXISTS student''')
conn.execute('''
    CREATE TABLE student (
        sid INTEGER NOT NULL,
        first_name VARCHAR(256) NOT NULL,
        last_name VARCHAR(256) NOT NULL,
        credits INTEGER NOT NULL,

        PRIMARY KEY (sid)
    );
''')
conn.commit()

conn.execute('''DROP TABLE IF EXISTS instructor''')
conn.execute('''
    CREATE TABLE instructor (
        tid INTEGER NOT NULL,
        first_name VARCHAR(256) NOT NULL,
        last_name VARCHAR(256) NOT NULL,
        dept VARCHAR(256) NOT NULL,

        PRIMARY KEY (tid)
    );
''')
conn.commit()

conn.execute('''DROP TABLE IF EXISTS course''')
conn.execute('''
    CREATE TABLE course (
        cid INTEGER NOT NULL,
        title VARCHAR(256) NOT NULL,
        tid INTEGER NOT NULL,

        PRIMARY KEY (cid),
        FOREIGN KEY (tid) REFERENCES instructor(tid)
    );
''')
conn.commit()

conn.execute('''DROP TABLE IF EXISTS enrolled''')
conn.execute('''
    CREATE TABLE enrolled (
        sid INTEGER NOT NULL,
        cid INTEGER NOT NULL,
        grade VARCHAR(256) NOT NULL,

        FOREIGN KEY (sid) REFERENCES student(sid),
        FOREIGN KEY (cid) REFERENCES course(cid)
    );
''')
conn.commit()

print("Tables created successfully")

# load preexisting tables 
table = pd.read_csv('./data/samplestudents.csv')
cur = conn.cursor()
for i, row in table.iterrows():
    params = (row.sid, row.first_name, row.last_name, row.credits)
    cur.execute('INSERT INTO student (sid, first_name, last_name, credits) VALUES(?, ?, ?, ?)', params)

table = pd.read_csv('./data/sampleinstructors.csv')
cur = conn.cursor()
for i, row in table.iterrows():
    params = (row.tid, row.first_name, row.last_name, row.dept)
    cur.execute('INSERT INTO instructor (tid, first_name, last_name, dept) VALUES(?, ?, ?, ?)', params)

table = pd.read_csv('./data/samplecourses.csv')
cur = conn.cursor()
for i, row in table.iterrows():
    params = (row.cid, row.title, row.tid)
    cur.execute('INSERT INTO course (cid, title, tid) VALUES(?, ?, ?)', params)

print("Sample tables loaded successfully")

conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows