# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Jaxon Evans
# Assignment Number: Assignment 5
# Due Date: 04/22/2026
# Purpose: We input our data table and calculate the averages of Thursday and Sunday
# Resources Used: Class slides, previous assignments, GeeksForGeeks, Python.org

import sqlite3

db = sqlite3.connect("temp_data.db")
c = db.cursor()

c.execute("drop table if exists temp_tab")
c.execute("create table temp_tab (id integer primary key, day text, temp real)")

f = open("Assignment5input.txt","r")

for x in f:
    parts = x.strip().split()
    d = parts[0]
    val = float(parts[1])

    c.execute("insert into temp_tab values (null, ?, ?)", (d, val))

f.close()

days = ["Sunday", "Thursday"]
avgs = []

for d in days:
    c.execute("select avg(temp) from temp_tab where day=?", (d,))
    res = c.fetchone()
    avgs.append(res[0])

sun = avgs[0]
thur = avgs[1]

print("Sunday average =", round(sun,2))
print("Thursday average =", round(thur,2))

db.commit()
db.close()
