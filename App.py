from flask import Flask , render_template ,request , redirect , url_for , flash
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
app = Flask(__name__)

app.secret_key = "Secret Key"


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Ruturaj8003#'
app.config['MYSQL_DB'] = 'mycrud'

mysql = MySQL(app)




@app.route('/')
def Index():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user")
    my_data = cursor.fetchall()
    return render_template('index.html' , employees = my_data)


@app.route('/insert' , methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO user(name , email , phone) VALUES(%s , %s , %s)", (name, email, phone))
        mysql.connection.commit()
        cursor.close()
        flash("Employee Inserted Successfully.")
        return  redirect(url_for('Index'))

@app.route('/update' , methods = ['GET' , 'POST'])
def update():
    if request.method == 'POST':
        id = request.form.get('id')
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE user SET name = %s , email = %s , phone = %s WHERE id = %s" , (name , email , phone , int(id)))
        mysql.connection.commit()
        flash("Employee updated successfully!!")
        return redirect(url_for('Index'))


@app.route('/delete/<id>/' , methods = ['GET'])
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM USER WHERE id = %s" , id)
    mysql.connection.commit()
    flash("Employee deleted successfully!!")
    return redirect(url_for('Index'))





if __name__ == "__main__":
    app.run(debug=True)