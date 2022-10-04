from flask import Flask, request, redirect, render_template
import sys
app = Flask(__name__)

@app.route('/') 
def index():
    from functions.sqlquery import sql_query
    return render_template('index.html')

# ---------------------------- students ----------------------------

@app.route('/student') 
def student_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM student''')
    msg = 'SELECT * FROM student'
    return render_template('studentdb.html', results=results, msg=msg)   

@app.route('/student/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_data_student_insert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        credits = request.form['credits']
        sql_edit_insert(''' INSERT INTO student (first_name,last_name,credits) VALUES (?,?,?) ''', \
                       (first_name,last_name,credits))
    results = sql_query(''' SELECT * FROM student''')
    msg = 'INSERT INTO student (first_name,last_name,credits) VALUES ('+first_name+','+last_name+','+credits+')'
    return render_template('studentdb.html', results=results, msg=msg) 

@app.route('/student/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_data_student_delete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        lname = request.args.get('lname')
        fname = request.args.get('fname')
        sql_delete(''' DELETE FROM student where first_name = ? and last_name = ?''', (fname,lname) )
    results = sql_query(''' SELECT * FROM student''')
    msg = 'DELETE FROM student WHERE first_name = ' + fname + ' and last_name = ' + lname
    return render_template('studentdb.html', results=results, msg=msg)

@app.route('/student/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_edit_student_link():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        elname = request.args.get('elname')
        efname = request.args.get('efname')
        eresults = sql_query2(''' SELECT * FROM student where first_name = ? and last_name = ?''', (efname,elname))
    results = sql_query(''' SELECT * FROM student''')
    return render_template('studentdb.html', eresults=eresults, results=results)

@app.route('/student/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_data_student_edit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_last_name = request.form['old_last_name']
        old_first_name = request.form['old_first_name']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        credits = request.form['credits']
        sql_edit_insert(''' UPDATE student set first_name=?,last_name=?,credits=? WHERE first_name=? and last_name=? ''', \
                       (first_name,last_name,credits,old_first_name,old_last_name) )
    results = sql_query(''' SELECT * FROM student''')
    msg = 'UPDATE student set first_name = ' + first_name + ', last_name = ' + last_name + ', credits = ' + credits + ' \
           WHERE first_name = ' + old_first_name + ' and last_name = ' + old_last_name
    return render_template('studentdb.html', results=results, msg=msg)

# ---------------------------- instructors ----------------------------

@app.route('/instructor') 
def instructor_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM instructor''')
    msg = 'SELECT * FROM instructor'
    return render_template('instructordb.html', results=results, msg=msg)   

@app.route('/instructor/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_data_instructor_insert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        dept = request.form['dept']
        sql_edit_insert(''' INSERT INTO instructor (first_name,last_name,dept) VALUES (?,?,?) ''', \
                       (first_name,last_name,dept))
    results = sql_query(''' SELECT * FROM instructor''')
    msg = 'INSERT INTO instructor (first_name,last_name,dept) VALUES ('+first_name+','+last_name+','+dept+')'
    return render_template('instructordb.html', results=results, msg=msg) 

@app.route('/instructor/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_data_instructor_delete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        lname = request.args.get('lname')
        fname = request.args.get('fname')
        sql_delete(''' DELETE FROM instructor where first_name = ? and last_name = ?''', (fname,lname) )
    results = sql_query(''' SELECT * FROM instructor''')
    msg = 'DELETE FROM instructor WHERE first_name = ' + fname + ' and last_name = ' + lname
    return render_template('instructordb.html', results=results, msg=msg)

@app.route('/instructor/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_edit_instructor_link():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        elname = request.args.get('elname')
        efname = request.args.get('efname')
        eresults = sql_query2(''' SELECT * FROM instructor where first_name = ? and last_name = ?''', (efname,elname))
    results = sql_query(''' SELECT * FROM instructor''')
    return render_template('instructordb.html', eresults=eresults, results=results)

@app.route('/instructor/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_data_instructor_edit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_last_name = request.form['old_last_name']
        old_first_name = request.form['old_first_name']
        last_name = request.form['last_name']
        first_name = request.form['first_name']
        dept = request.form['dept']
        sql_edit_insert(''' UPDATE instructor set first_name=?,last_name=?,dept=? WHERE first_name=? and last_name=? ''', \
                       (first_name,last_name,dept,old_first_name,old_last_name) )
    results = sql_query(''' SELECT * FROM instructor''')
    msg = 'UPDATE instructor set first_name = ' + first_name + ', last_name = ' + last_name + ', dept = ' + dept + ' \
           WHERE first_name = ' + old_first_name + ' and last_name = ' + old_last_name
    return render_template('instructordb.html', results=results, msg=msg)

# ---------------------------- courses ----------------------------

@app.route('/course') 
def course_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM course''')
    tresults = sql_query(''' SELECT * FROM instructor''')
    msg = 'SELECT * FROM course'
    return render_template('coursedb.html', results=results, tresults=tresults, msg=msg)   

@app.route('/course/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_data_course_insert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        tid = request.form['tid']
        title = request.form['title']
        sql_edit_insert(''' INSERT INTO course (title,tid) VALUES (?,?) ''', \
                       (title,tid))
    results = sql_query(''' SELECT * FROM course''')
    tresults = sql_query(''' SELECT * FROM instructor''')
    msg = 'INSERT INTO course (title,tid) VALUES ('+title+','+tid+')'
    return render_template('coursedb.html', results=results, tresults=tresults, msg=msg) 

@app.route('/course/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_data_course_delete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        tid = request.args.get('tid')
        title = request.args.get('title')
        sql_delete(''' DELETE FROM course where title = ? and tid = ?''', (title,tid) )
    results = sql_query(''' SELECT * FROM course''')
    tresults = sql_query(''' SELECT * FROM instructor''')
    msg = 'DELETE FROM course WHERE title = ' + title + ' and tid = ' + tid
    return render_template('coursedb.html', results=results, tresults=tresults, msg=msg)

@app.route('/course/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_edit_course_link():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        etid = request.args.get('etid')
        etitle = request.args.get('etitle')
        eresults = sql_query2(''' SELECT * FROM course where title = ? and tid = ?''', (etitle,etid))
    results = sql_query(''' SELECT * FROM course''')
    tresults = sql_query(''' SELECT * FROM instructor''')
    return render_template('coursedb.html', eresults=eresults, results=results, tresults=tresults)

@app.route('/course/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_data_course_edit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_tid = request.form['old_tid']
        old_title = request.form['old_title']
        tid = request.form['tid']
        title = request.form['title']
        sql_edit_insert(''' UPDATE course set title=?,tid=? WHERE title=? and tid=? ''', \
                       (title,tid,old_title,old_tid) )
    results = sql_query(''' SELECT * FROM course''')
    tresults = sql_query(''' SELECT * FROM instructor''')
    msg = 'UPDATE course set title = ' + title + ', tid = ' + tid +' \
           WHERE title = ' + old_title + ' and tid = ' + old_tid
    return render_template('coursedb.html', results=results, tresults=tresults, msg=msg)

# ---------------------------- enrollment ----------------------------


@app.route('/enroll') 
def enroll_database():
    from functions.sqlquery import sql_query
    results = sql_query(''' SELECT * FROM enroll JOIN student JOIN course ON enroll.sid = student.sid AND enroll.cid = course.cid''')
    sresults = sql_query(''' SELECT * FROM student''')
    cresults = sql_query(''' SELECT * FROM course''')
    msg = 'SELECT * FROM enroll'
    return render_template('enrolldb.html', results=results, sresults=sresults, cresults=cresults, msg=msg)   

@app.route('/enroll/insert',methods = ['POST', 'GET']) #this is when user submits an insert
def sql_data_enroll_insert():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        sid = request.form['sid']
        cid = request.form['cid']
        grade = request.form['grade']
        sql_edit_insert(''' INSERT INTO enroll (sid,cid, grade) VALUES (?,?,?) ''', \
                       (sid,cid,grade))
    results = sql_query(''' SELECT * FROM enroll JOIN student JOIN course ON enroll.sid = student.sid AND enroll.cid = course.cid''')
    sresults = sql_query(''' SELECT * FROM student''')
    cresults = sql_query(''' SELECT * FROM course''')
    msg = 'INSERT INTO enroll (sid,cid,grade) VALUES ('+sid+','+cid+','+grade+')'
    return render_template('enrolldb.html', results=results, sresults=sresults, cresults=cresults, msg=msg)

@app.route('/enroll/delete',methods = ['POST', 'GET']) #this is when user clicks delete link
def sql_data_enroll_delete():
    from functions.sqlquery import sql_delete, sql_query
    if request.method == 'GET':
        sid = request.args.get('sid')
        cid = request.args.get('cid')
        sql_delete(''' DELETE FROM enroll where cid = ? and sid = ?''', (cid,sid) )
    results = sql_query(''' SELECT * FROM enroll JOIN student JOIN course ON enroll.sid = student.sid AND enroll.cid = course.cid''')
    sresults = sql_query(''' SELECT * FROM student''')
    cresults = sql_query(''' SELECT * FROM course''')
    msg = 'DELETE FROM enroll WHERE cid = ' + cid + ' and sid = ' + sid
    return render_template('enrolldb.html', results=results, sresults=sresults, cresults=cresults, msg=msg)

@app.route('/enroll/query_edit',methods = ['POST', 'GET']) #this is when user clicks edit link
def sql_edit_enroll_link():
    from functions.sqlquery import sql_query, sql_query2
    if request.method == 'GET':
        esid = request.args.get('esid')
        ecid = request.args.get('ecid')
        eresults = sql_query2(''' SELECT * FROM enroll where cid = ? and sid = ?''', (ecid,esid))
    results = sql_query(''' SELECT * FROM enroll JOIN student JOIN course ON enroll.sid = student.sid AND enroll.cid = course.cid''')
    sresults = sql_query(''' SELECT * FROM student''')
    cresults = sql_query(''' SELECT * FROM course''')
    return render_template('enrolldb.html', eresults=eresults, results=results, sresults=sresults, cresults=cresults)

@app.route('/enroll/edit',methods = ['POST', 'GET']) #this is when user submits an edit
def sql_data_enroll_edit():
    from functions.sqlquery import sql_edit_insert, sql_query
    if request.method == 'POST':
        old_sid = request.form['old_sid']
        old_cid = request.form['old_cid']
        sid = request.form['sid']
        cid = request.form['cid']
        grade = request.form['grade']
        sql_edit_insert(''' UPDATE enroll set cid=?,sid=?, grade=? WHERE cid=? and sid=? ''', \
                       (cid,sid,grade,old_cid,old_sid) )
    results = sql_query(''' SELECT * FROM enroll JOIN student JOIN course ON enroll.sid = student.sid AND enroll.cid = course.cid''')
    sresults = sql_query(''' SELECT * FROM student''')
    cresults = sql_query(''' SELECT * FROM course''')
    msg = 'UPDATE enroll set cid = ' + cid + ', sid = ' + sid +' \
           WHERE cid = ' + old_cid + ' and sid = ' + old_sid
    return render_template('enrolldb.html', results=results, sresults=sresults, cresults=cresults, msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
