from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def init_db():
    conn = sqlite3.connect('highbank.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL,
        senha TEXT NOT NULL
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        type TEXT NOT NULL,
        amount REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_account', methods=['POST'])
def create_account():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    
    conn = sqlite3.connect('highbank.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
    conn.commit()
    conn.close()

    flash('Conta criada com sucesso!', 'success')
    return redirect(url_for('account'))

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if request.method == 'POST':
        account_destino = request.form['account-destino']
        valor = request.form['valor']
        # Aqui você pode adicionar a lógica para registrar a transação no banco de dados
        flash('Transferência realizada com sucesso!', 'success')
        return redirect(url_for('account'))
    return render_template('transfer.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    if request.method == 'POST':
        valor = request.form['valor']
        # Lógica para registrar a transação no banco de dados
        flash('Saque realizado com sucesso!', 'success')
        return redirect(url_for('account'))
    return render_template('withdraw.html')

@app.route('/recharge', methods=['GET', 'POST'])
def recharge():
    if request.method == 'POST':
        valor = request.form['valor']
        # Lógica para registrar a transação no banco de dados
        flash('Recarga realizada com sucesso!', 'success')
        return redirect(url_for('account'))
    return render_template('recharge.html')

@app.route('/card', methods=['GET', 'POST'])
def card():
    if request.method == 'POST':
        # Lógica para registrar o pedido de cartão
        flash('Pedido de cartão realizado com sucesso!', 'success')
        return redirect(url_for('account'))
    return render_template('card.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
