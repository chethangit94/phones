import MySQLdb
from flask import Flask
from flask import jsonify
app = Flask(__name__)

def get_phone_list():
	# Connect
	db = MySQLdb.connect(host="localhost",
			     user="root",
			     passwd="",
			     db="phones")

	cursor = db.cursor()

	# Execute SQL select statement
	cursor.execute("SELECT * FROM phone")

	# Commit your changes if writing
	# In this case, we are only reading data
	# db.commit()

	# Get the number of rows in the resultset
	numrows = cursor.rowcount
	phone_list = {}
	# Get and display one row at a time
	for x in range(0, numrows):
	    row = cursor.fetchone()
	    print (row[0], "-->", row[1])
	    phone_list[row[0]] = row[1]
        print "closing db connection" 
	# Close the connection
	db.close()
	return phone_list

@app.route('/')
def hello():
    return "welcome to world of mobiles!"
@app.route('/phonelist')
def phonelist():
    return jsonify(get_phone_list())
if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)

