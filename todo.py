from flask import Flask
from flask import send_file
from flask import render_template
from flask import request
import os
from flask import session
import datetime
from datetime import datetime
from datetime import date
from datetime import time 
from flask import redirect


app = Flask(__name__)
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
# End of opening

@app.route('/')
def home():
	import sqlite3
	connection = sqlite3.connect("todo.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM todo WHERE status == 'todo'")
	rows = cursor.fetchall()
	return render_template('home.html', rows=rows)

@app.route('/newtodo', methods=['POST'])
def newtodo():
	import sqlite3
	connection = sqlite3.connect("todo.db")
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	newtodo = request.form['newtodo']
	newnotes = request.form['newnotes']
	newtags = request.form['newtags']
	status = "todo"
	cursor.execute("INSERT INTO todo (todo, notes, tags, status) \
		VALUES (?, ?, ?, ?)", (newtodo, newnotes, newtags, status))
	connection.commit()
	return redirect('/')

@app.route('/updatestatus/<ID>', methods=['POST'])
def updatestatus(ID):
		import sqlite3
		connection = sqlite3.connect('todo.db')
		cursor = connection.cursor()
		updatestatus = request.form['updatestatus']
		cursor.execute("UPDATE todo SET status = ? WHERE ID == ?", (updatestatus, ID))
		connection.commit()
		return redirect('/')


# Close Flask
if __name__ == '__main__':
   app.run(debug = True)