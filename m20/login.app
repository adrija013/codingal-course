import mysql.connector

@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
            host = "remotemyql.com",
            user = "Rz8hqnldk4",
            password="nd0wK03XE0",
            database="Rz8hqnldk4"
        )

        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name = %s AND Password = %s",(username, password))
        account = mycursor.fethone()
        if account():
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Succesfully'
            print('login successful!')
            return render_template('index.html')
        else:
            msg = 'incorrect credentials. Kindly check.'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html')