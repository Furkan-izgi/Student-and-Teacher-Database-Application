import sqlite3

#Students database

def connect_student():
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY,ns text,school_number integer)")
    conn.commit()
    conn.close()

def insert_student(ns, school_number):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO students VALUES (NULL,?,?)",(ns,school_number))
    conn.commit()
    conn.close()
    view_student()

def view_student():
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM students")
    rows=cur.fetchall()
    conn.close()
    return rows

def search_student(ns = "",school_number = ""):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM students WHERE ns = ? OR school_number = ? ", (ns,school_number))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_student(id):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM students WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update_student(id, ns, school_number):
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("UPDATE students SET ns = ?,school_number = ? WHERE id = ?",(ns,school_number,id))
    conn.commit()
    conn.close()
    
connect_student()
   
#Teachers database 
    
def connect_teacher():
    conn=sqlite3.connect("teacher.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS teachers (id INTEGER PRIMARY KEY,ns text,lesson text)")
    conn.commit()
    conn.close()

def insert_teacher(ns, lesson):
    conn=sqlite3.connect("teacher.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO teachers VALUES (NULL,?,?)",(ns,lesson))
    conn.commit()
    conn.close()
    view_teacher()

def view_teacher():
    conn=sqlite3.connect("teacher.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM teachers")
    rows=cur.fetchall()
    conn.close()
    return rows

def search_teacher(ns = "",lesson = ""):
    conn=sqlite3.connect("teacher.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM teachers WHERE ns = ? OR lesson = ? ", (ns,lesson))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete_teacher(id):
    conn=sqlite3.connect("teacher.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM teachers WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update_teacher(id, ns, lesson):
    conn=sqlite3.connect("teacher.db")
    cur=conn.cursor()
    cur.execute("UPDATE teachers SET ns = ?,lesson = ? WHERE id = ?",(ns,lesson,id))
    conn.commit()
    conn.close()

connect_teacher()