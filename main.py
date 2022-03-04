from flask import Flask, redirect, render_template, request
import sqlite3


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def signin():
    
    if request.method == 'POST':
        user_email = request.form.get('mailid')
        user_password = request.form.get('password')
        
        valid_user = varify_user(user_email,user_password)
        if valid_user == "True":
           return redirect('/addcontact?emailid='+user_email)

    return render_template("signinpage.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('mailid')
        password = request.form.get('password')
        secret_key = request.form.get('secretcode')
        create_user(email,password,secret_key)
        return redirect('/addcontact?emailid='+email)
          
    return render_template("signuppage.html")

@app.route('/addcontact', methods=['GET', 'POST'])
def addcontact():
    user_email = request.args.get('emailid')
    if request.method == 'POST':
        contact_name = request.form.get('name')
        contact_number = request.form.get('number')
        contact_email = request.form.get('email')
        add_contacts(user_email,contact_name,contact_email,contact_number)
        # view_contacts(user_email)
        # return redirect('/addcontact?emailid='+email)
    print('login email id: '+user_email)
    html_contacts = view_contacts(user_email)
    return render_template("addcontact.html",contact_rows = html_contacts)

@app.route('/createtable')
def createtable():
    create_user_tables()
    create_contact_tables()
    return "table created"

def create_user_tables():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE USER
         (EMAIL_ID TEXT NOT NULL,
          PASSWORD TEXT NOT NULL,
          SECRET_KEY TEXT NOT NULL);''')
    print(" User table created successfully")

    conn.close()

def create_contact_tables():
    conn = sqlite3.connect('test.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE CONTACT
         (USER_EMAIL_ID TEXT NOT NULL,
          CONTACT_NAME TEXT NOT NULL,
          CONTACT_EMAIL_ID TEXT NOT NULL,
          CONTACT_NUMBER TEXT NOT NULL);''')
    print(" Contact table created successfully")

    conn.close()

def create_user(email,password,secret_key):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    print("Opened database successfully")

    cur.execute('INSERT INTO USER VALUES (?, ?, ?)',(email,password,secret_key))

    conn.commit()
    print(email, " added to user table")

    conn.close()

def add_contacts(user_email,contact_name,contact_email,contact_number):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    print("Opened database successfully")

    cur.execute('INSERT INTO CONTACT VALUES (?, ?, ?, ?)',(user_email,contact_name,contact_email,contact_number))

    conn.commit()
    print(contact_name, " added to contact table")

    conn.close()

def view_contacts(user_email):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    html_rows = " "
    print("Opened database successfully")

    
    for row in cur.execute('SELECT * FROM CONTACT WHERE USER_EMAIL_ID=?',[user_email]):
        print(row)
        html_rows += "<tr>"  
        html_rows += '<td>"' + row[1] + '"</td>'
        html_rows += '<td>"' + row[2] + '"</td>'
        html_rows += '<td>"' + row[3] + '"</td>'
        html_rows += "</tr>"

    print(html_rows)
    conn.commit()
    print(user_email, "list user's contacts")

    conn.close()
    return html_rows

def varify_user(user_email,user_password):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    valid_user = "False"
    print("Opened database successfully")
    print(user_email+"   "+user_password)

    
    cur.execute('SELECT * FROM USER WHERE EMAIL_ID=? AND PASSWORD=?',(user_email,user_password))
    if not cur.fetchone():  # An empty result evaluates to False.
        print("Login failed")
        valid_user = "False"
    else:
         print("Welcome")
         valid_user = "True"
        

    conn.commit()
    print(user_email, "list user's contacts")

    conn.close() 
    return valid_user



if "__name__" == "__main__":
    app.run(debug=True)

