from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='stocks'
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM stocks')
    stocks = cursor.fetchall()
    conn.close()
    return render_template('index.html', stocks=stocks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        price = request.form['price']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO stocks (item_name, quantity, price) VALUES (%s, %s, %s)',
                       (item_name, quantity, price))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    return render_template('add.html', stock=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM stocks WHERE id = %s', (id,))
    stock = cursor.fetchone()

    if request.method == 'POST':
        item_name = request.form['item_name']
        quantity = request.form['quantity']
        price = request.form['price']

        cursor.execute('UPDATE stocks SET item_name=%s, quantity=%s, price=%s WHERE id=%s',
                       (item_name, quantity, price, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', stock=stock)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM stocks WHERE id = %s', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
